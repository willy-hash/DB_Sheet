from Connection.ConnectionSheet import ConnectionSheet
import logging

logger_instance = logging.getLogger(__name__)
Connection = ConnectionSheet()

class QueriesMain:
    worksheet = Connection.get_Sheet()
    logger = logger_instance

    def get_all(self):
        try:
            return self.worksheet.get_all_records()
        except Exception as e:
            self.logger.warning(f" 'Method - get_all()' - 'Get values' Error to get values - {e}")

    def add(self, values: list, uid: str) -> bool:
        rows = None
        try:
            rows = self.get_all()
            last_row = len(rows) + 1

            newRow = values + [uid]

            self.worksheet.update([newRow], f'A{last_row}:C{last_row}')
            return True

        except Exception as e:
            if rows is not None:
                self.logger.warning(f" 'Method - add()' - 'Error to add row' - {e}")
            else:
                self.logger.warning(f" 'Method - add()' - 'Error to get values row' - {e}")
            return False

    def update(self, uid: str, values: list) -> bool:
        cell = None
        try:
            cell = self.worksheet.find(uid)
            self.worksheet.update([values], f"A{cell.row}:B{cell.row}")
            return True

        except Exception as e:
            if cell is not None:
                self.logger.warning(f" 'Method - update()' - 'Error to update row' - {e}")
            else:
                self.logger.warning(f" 'Method - update()' - 'Not found' Uid '{uid}'  - {e}" )

            return False

    def remove(self, uid : str) -> bool:
        cell = None
        try:
            cell = self.worksheet.find(uid)
            self.worksheet.update([["", "", ""]], f"A{cell.row}:C{cell.row}")
            return True

        except Exception as e:
            if cell is not None:
                self.logger.warning(f" 'Method - remove()' - 'Error to remove row' - {e}")
            else:
                self.logger.warning(f" 'Method - remove()' - 'Not found' Uid '{uid}' for remove - {e}")
            return False