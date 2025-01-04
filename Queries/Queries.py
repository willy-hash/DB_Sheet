from Connetion.ConnectionSheet import ConnectionSheet

Connection = ConnectionSheet()

class Queries:
    worksheet = Connection.get_Sheet()

    def get_all(self):
        return self.worksheet.get_all_records()

    def add(self, values: list, uid: str) -> bool:
        try:
            rows = self.get_all()
            last_row = len(rows) + 1

            newRow = values + [uid]

            self.worksheet.update([newRow], f'A{last_row}:C{last_row}')
            return True

        except Exception as e:
            print(f"Putting in logging , {e}")
            return False

    def update(self, uid: str, values: list) -> bool:
        try:
            cell = self.worksheet.find(uid)
            self.worksheet.update([values], f"A{cell.row}:B{cell.row}")
            return True

        except Exception as e:
            print(f"Putting in logging , {e}")
            return False

    def remove(self, uid : str) -> bool:
        try:
            cell = self.worksheet.find(uid)
            self.worksheet.update([["", "", ""]], f"A{cell.row}:C{cell.row}")
            return True

        except Exception as e:
            print(f"Putting in logging , {e}")
            return False