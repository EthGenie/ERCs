import argparse
from erc_check.build_index import build_index
from erc_check.search import search_similar

def main():
    parser = argparse.ArgumentParser(description="Search for similar EIPs/ERCs based on draft input.")
    subparsers = parser.add_subparsers(dest="command")

    build_cmd = subparsers.add_parser("build", help="Build the EIP/ERC index")
    build_cmd.add_argument("--eip-dir", type=str, default="./ERCS", help="Path to folder with EIP/ERC markdown files")

    search_cmd = subparsers.add_parser("search", help="Search similar EIPs")
    search_cmd.add_argument("--text", type=str, required=True, help="Your abstract or spec snippet")

    args = parser.parse_args()

    if args.command == "build":
        build_index(eip_folder=args.eip_dir)
    elif args.command == "search":
        results = search_similar(args.text)
        print("\nTop similar EIPs:")
        for title, file in results:
            print(f"📄 {title} ({file})")
    else:
        parser.print_help()
