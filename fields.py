# MIT License

# Copyright (c) 2022 Georgios Papachristou

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from collections import namedtuple


fields = ('input_name', 'exported_name', 'type')
defaults = (' ', ' ', 'object')
field = namedtuple('field', fields, defaults=defaults)


class Field:
    """
    Field class includes all the used dataframe fields.

    Each field is a Python namedtuple object with 2 fields.
        * input_name: Is the actual name of the field in pandas column
        * exported_name: Is a human readable version of the pandas column name.
          This field is suggested to used only before export the final dataframe.
        * type: Column data type

    ---- Recommended naming conventions ----
        * field name: Python snake case convention (e.g product_name)
        * input_name: No specific convention is followed, depends on the source (e.g DummyColumn)
        * exported_name: Follow export fields conventions. Rules:
            - Capitalize first letter in each word except 'by' and 'of'
            - Space between words
            - Do not use special characters (e.g slashes, spaces, periods)
    """
    # Field example
    dummy_field = field(input_name='dummy_column_1', exported_name='Dummy Column', type='int32')
    dummy_field_2 = field(input_name='dummy_column_2', exported_name='Dummy Column 2')

    # ....
    # ...
    # ..

    @classmethod
    def get_fields(cls):
        """
        Creates a dictionary with key the input_name and value the field nametuple
        e.g {'DummyColumn': field(input_name='DummyColumn', ...), ... }
        :return: dict
        """
        fields = {}
        for attribute in cls.__dict__.keys():
            if attribute[:2] != '__':
                field = getattr(cls, attribute)
                if not callable(field):
                    fields[field.input_name] = field
        return fields

    @classmethod
    def get_field(cls, input_name):
        """
        Get field nametuple obj by using input_name
        :return: nametuple
        """
        fields = cls.get_fields()
        return fields[input_name]

    @classmethod
    def get_renames(cls):
        """
        Creates a dictionary with all the fields mapping between input_name to exported_name
        e.g {'DummyColumn1': 'Dummy Column 1', 'DummyColumn2': 'Dummy Column 2', ... }
        :return: dict
        """
        fields = cls.get_fields()
        return {input_name: field.exported_name for input_name, field in fields.items()}

    @classmethod
    def get_rename(cls, input_name):
        """
        Get field exported_name by using input_name
        :return: str
        """
        renames = cls.get_renames()
        return renames[input_name]

    @classmethod
    def get_fields_cast(cls, columns):
        """
        Creates a dictionary with all the fields mapping between input_name to type
        e.g {'DummyColumn1': 'int32', 'DummyColumn2': object, ... }
        :return: dict
        """
        col_fields = [cls.get_field(col) for col in columns]
        return {col_field.input_name:col_field.type for col_field in col_fields}
