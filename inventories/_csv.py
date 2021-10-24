from pandas import read_csv
from re import sub
from pathlib import Path

from .inventory import Inventory


REGEX_ACCEPTED_EXTENSIONS = '*.[cC][sS][vV]'
DIR = 'directory'
FILE = 'file'
CSV_COLUMN_PRODUCT_ID = 'productID'
CSV_COLUMN_PRODUCT_TITLE = 'productTitle'
CSV_COLUMN_PRODUCT_QUANTITY = 'productQuantity'

INVENTORY_TITLE = 'title'
INVENTORY_ID = 'id'
INVENTORY_QUANTITY = 'qty'


class Csv(Inventory):
    config_data_type = {
            FILE: Path,
            DIR: Path,
            CSV_COLUMN_PRODUCT_ID: list,
            CSV_COLUMN_PRODUCT_TITLE: str,
            CSV_COLUMN_PRODUCT_QUANTITY: str
        }

    def validate_config(self, **kwargs) -> bool:
        """
        Required config:
            - filename (Takes Priority)
            -- or
            - directory

        :param kwargs:
        """

        try:
            self.__validate_target_path(kwargs[FILE], FILE)
        except KeyError:
            try:
                self.__validate_target_path(kwargs[DIR], DIR)
            except KeyError:
                raise Exception("Expecting 'file' or 'directory' values; none were found")

        try:
            kwargs[CSV_COLUMN_PRODUCT_ID]
        except KeyError:
            raise Exception("Expecting 'productID' values; none were found")

        try:
            kwargs[CSV_COLUMN_PRODUCT_TITLE]
        except KeyError:
            raise Exception("Expecting 'productTitle' values; none were found")

        try:
            kwargs[CSV_COLUMN_PRODUCT_QUANTITY]
        except KeyError:
            raise Exception("Expecting 'productQuantity' values; none were found")

    @staticmethod
    def __validate_target_path(path, expected_type):
        path = Path(path)
        expected_types_map = {
            FILE: path.is_file,
            DIR: path.is_dir
        }

        if not path.exists():
            raise Exception(f"Path, {path}, does not exist; please choose a valid path.")

        if not expected_types_map[expected_type]():
            raise Exception(f"Path, {path}, is declared to be a {expected_type}, but is not.")

    def set_inventory(self):
        target_file = self._select_target_file()
        self.inventory = self.__get_csv_data(target_file)

    def __get_csv_data(self, target_file):
        csv_data = read_csv(target_file)
        inventory_data = []

        for index, row in csv_data.iterrows():
            inventory_data.append(
                {
                    INVENTORY_ID: self.__extract_inventory_id_from_csv(row, self.config[CSV_COLUMN_PRODUCT_ID]),
                    INVENTORY_TITLE: str(row[self.config[CSV_COLUMN_PRODUCT_TITLE]]),
                    INVENTORY_QUANTITY: float(row[self.config[CSV_COLUMN_PRODUCT_QUANTITY]])
                }
            )

        return inventory_data

    @staticmethod
    def __extract_inventory_id_from_csv(row, csv_columns):
        def __clean_inventory_id(id_val):
            clean_list = [
                __remove_prefix_symbols,
                __remove_suffix_symbols
            ]

            for task in clean_list:
                id_val = task(id_val)

            return id_val

        def __remove_prefix_symbols(s):
            return sub(r'^=\"', '', s)

        def __remove_suffix_symbols(s):
            return sub(r'\"$', '', s)

        def __remove_appended_comma(s):
            return sub(r',$', '', s)

        inventory_ids = ''
        for column in csv_columns:
            inventory_ids += f"{__clean_inventory_id(row[column])},"

        inventory_ids = __remove_appended_comma(inventory_ids)

        return inventory_ids

    def _select_target_file(self):
        """
        Selection Logic/Priority:
            See if Directory is available
                T: Request user to specify file
                F: Use 'File' value

        :return: Path
        """
        if self.__is_directory_set():
            available_files = list(self.config[DIR].rglob(REGEX_ACCEPTED_EXTENSIONS))
            return self.__user_request_specific_file(available_files)
        else:
            return self.config[FILE]

    @staticmethod
    def __user_request_specific_file(available_files):
        def __validate_user_input(__selection, __max_selection_num):
            if 0 <= __selection <= __max_selection_num:
                return 1
            return 0

        def __list_available_files():
            print(f"Available Files:")
            for index, file in enumerate(available_files):
                print(f'\t{index}.) {file}')

        valid_input = 0
        __list_available_files()

        while not valid_input:
            try:
                selected_file = int(input("Enter # for specific file to load. \n# "))
            except ValueError:
                selected_file = -1

            if __validate_user_input(selected_file, len(available_files)):
                valid_input = 1
            else:
                print(f"#{selected_file} is not an available file - please try again.")

        return available_files[selected_file]

    def __is_directory_set(self):
        try:
            self.get_config(DIR)
            return 1
        except Exception:
            return 0



