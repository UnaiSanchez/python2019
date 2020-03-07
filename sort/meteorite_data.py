import sv_data_processor
from collections import namedtuple
def main():
    opened_file = sv_data_processor.open_separated_value_file("datasets\mystery_data.tsv")
    Meteor = namedtuple("Meteor",next(opened_file))
    piped_values = sv_data_processor.pipe_separated_valued([[
        str,int,str,int,str,str,float,float,str
    ]])
    meteorites = map(lambda data:sv_data_processor.apply_namedtuple(Meteor,data),piped_values)

main()