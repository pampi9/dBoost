import pathlib
import sys

if __name__ == "__main__" and __package__ is None:
    from os import path, sys

    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    sys.path.append(pathlib.Path(__file__).parent)
from dboost import cli, outliers, utils

parser = cli.get_stdin_parser()
args, models, analyzers, rules = cli.parsewith(parser)

testset_generator = utils.stream_tuples(
    args.input, args.fs, args.floats_only, args.inmemory, args.maxrecords
)
trainset_generator = testset_generator

outliers(
    trainset_generator,
    testset_generator,
    analyzers[1],
    models[0],
    rules,
    args.runtime_progress,
    args.maxrecords,
)
