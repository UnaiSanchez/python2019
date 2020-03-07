from os.path import isfile
accepted_filetypes = {
    "csv":",",
    "tsv":"\t"
}
def open_separated_value_file(filename):
    if not isfile(filename):
        return None
    filetype =filename.partition(".")[2]
    if not filetype in accepted_filetypes:
        raise NotImplementedError
    try:
        file = open(filename,"r")
    except:
        file = open(filename,"r",encoding="utf-8")
        yield next(file)
        for line in file:
            yield line.strip().split(accepted_filetypes[filetype])
def pipe_separated_values(pipeline, values):
    for pipe in pipeline:
        for processor, item in zip(pipe,next(values)):
            yield processor(item)
def apply_namedtuple(named_tuple,data):
    return named_tuple(*data)
if __name__ == "__main__":
    opened_file = open_separated_value_file("datasets\data_person_1000000.csv")
    from collections import namedtuple
    from pprint import print
    Person = namedtuple("Person", next(opened_file))
    piped_valuez = pipe_separated_values([[
        str,
        str,
        float,
        int,
        str
    ]], opened_file)
