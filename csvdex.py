from tools.scrape_dex_csv import scrape_dex_csv
from tools.scrape_move_list import scrape_move_list
from tools.scrape_dex_moves import scrape_dex_moves
import argparse

def update_csv_data():
    scrape_dex_csv("data")
    scrape_move_list("data")
    scrape_dex_moves("data")


if __name__ == "__main__":
    print("===== CSV_DEX v0.6.0 =====")
    parser = argparse.ArgumentParser(description='Collect Pokemon data')
    parser.add_argument('--update-data', '-u', action='store_true', help="Update all CSV data files.")

    args = parser.parse_args()
    
    if args.update_data == True:
        print("==> Updating CSV data...")
        update_csv_data()