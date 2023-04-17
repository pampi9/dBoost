import bisect
import os
import sys
from io import StringIO

from . import color


std_out = StringIO()


def debug(*args, **kwargs):
    kwargs["file"] = sys.stderr
    print(*args, **kwargs)


def report_progress(nb):
    if nb % 1000 == 0:
        print(nb, end="\r", file=sys.stderr)


def expand_hints(fields_group, hints):
    expanded_group = []

    for field_id, feature_id in fields_group:
        if field_id == 0:
            expanded_group.extend(hints[feature_id])
        else:
            expanded_group.append((field_id - 1, feature_id))

    return tuple(expanded_group)


def describe_discrepancy(fields_group, rules_descriptions, hints, x):
    expanded = expand_hints(fields_group, hints)

    field_ids, values, features = zip(
        *(
            (field_id, x[field_id], rules_descriptions[type(x[field_id])][feature_id])
            for field_id, feature_id in expanded
        )
    )

    if len(expanded) == 1:
        FMT = "   > Value '{}' ({}) doesn't match feature '{}'"
        msg = FMT.format(values[0], field_ids[0], features[0])
    else:
        FMT = "   > Values {} {} do not match features {}"
        msg = FMT.format(values, field_ids, features)

    return msg, features


def store_result(outliers, model, hints, rules_descriptions):
    features = []
    for linum, (x, X, discrepancies) in outliers:
        for fields_group in discrepancies:
            output = {"from": None, "to": None}
            ((field_id1, feature_id1), (field_id2, feature_id2)) = expand_hints(fields_group, hints)
            for field_id, feature_id in [(field_id1, feature_id1), (field_id2, feature_id2)]:
                histograms = {}
                for value, hist in model.all_counters[feature_id].items():
                    if value not in histograms:
                        histograms[value] = []
                    histograms[value].append(hist)
                output["from" if output["from"] is None else "to"] = {
                    "field_id": field_id,
                    "rule": rules_descriptions[type(x[field_id])][feature_id],
                    "hist": histograms
                }
            if output["from"]["field_id"] == 3 and output["to"]["field_id"] == 4:
                if output["from"]["rule"] == "empty" and output["to"]["rule"] == "strp":
                    pass
                    # print("EXPANDED", output)
                if output["from"]["rule"] == "is digit" and output["to"]["rule"] == "strp":
                    print("EXPANDED", output)
            features.append(output)
    exit()
    for feature in features:
        print(feature)
    exit()


def print_rows(
    outliers, model, hints, rules_descriptions, verbosity=0, max_w=40, header="   "
):
    # store_result(outliers, model, hints, rules_descriptions)
    if len(outliers) == 0:
        return

    output = []

    # each outlier is (x, X, discrepancies)
    nb_fields = len(outliers[0][1][0])
    widths = (0,) * nb_fields

    # Compute the ideal column width for each column
    for _, (x, _, _) in outliers:
        widths = tuple(max(w, min(max_w, len(str(f)))) for w, f in zip(widths, x))

    for linum, (x, X, discrepancies) in outliers:
        output_discrepancy = []
        highlight = [
            field_id
            for fields_group in discrepancies
            for field_id, _ in expand_hints(fields_group, hints)
        ]

        truncated_x = tuple(str(f)[:w] for f, w in zip(x, widths))
        padding = tuple(w - len(f) for f, w in zip(truncated_x, widths))
        colorized_x = colorize(truncated_x, highlight)
        colorized_x = " ".join(f + " " * p for f, p in zip(colorized_x, padding))

        if verbosity < 0:
            output_discrepancy.append(str(linum))
            # sys.stdout.write(str(linum) + "\n")
        else:
            output_discrepancy.append(header + colorized_x)
            # sys.stdout.write(header + colorized_x + "\n")

            if verbosity > 0:
                for fields_group in discrepancies:
                    msg, features_desc = describe_discrepancy(
                        fields_group, rules_descriptions, hints, x
                    )
                    output_discrepancy.append(msg)
                    # sys.stdout.write(msg + "\n")

                    if verbosity > 1:
                        model.more_info(
                            discrepancy=fields_group,
                            description=features_desc,
                            X=X,
                            indent="     ",
                            # pipe=std_out,
                        )
                        # std_out.write("\n\n")
                output_discrepancy.append(std_out.getvalue())
                # sys.stdout.write("\n")
            output.append(output_discrepancy)
    return output


def colorize(row, indices):
    row = [str(f) for f in row]
    for index in indices:
        row[index] = color.highlight(row[index], color.term.UNDERLINE)
    return row


def hhistplot(counter, highlighted, indent="", pipe=sys.stdout, w=20):
    BLOCK = "█"
    LEFT_HALF_BLOCK = "▌"

    try:
        W, H = os.get_terminal_size()
    except (OSError, AttributeError):
        W, H = 80, 24

    plot_w = min(w, W - 10 - len(indent))
    scale = plot_w / max(counter.values())
    data = sorted(counter.items())

    if highlighted != None and highlighted not in counter:
        bisect.insort_left(data, (highlighted, 0))

    header_width = max(len(str(value)) for _, value in data)

    for key, value in data:
        label = str(key)
        bar_size = int(value * scale)
        header = indent + "[" + str(value).rjust(header_width) + "] "
        bar = (BLOCK * bar_size if bar_size > 0 else LEFT_HALF_BLOCK) + " "

        label_avail_space = W - 2 - len(bar) - len(header)
        if len(label) > label_avail_space:
            label = label[: label_avail_space - 3] + "..."

        line = bar + label
        if key == highlighted:
            line = color.highlight(line, color.term.PLAIN, color.term.RED)

        pipe.write(header + line + "\n")
