# main.py
import os
from summary_pipeline import process_pdfs




def main():
input_dir = "input_pdfs"
output_dir = "output_docs"


os.makedirs(input_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)


process_pdfs(input_dir, output_dir)




if __name__ == "__main__":
main()
