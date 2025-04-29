import argparse
import sys
import modules.scanner as scanner
import modules.proxy_scraper as proxy_scraper
import modules.ip_lookup_tool as ip_lookup
import modules.reverse_shell_generator as reverse_shell

TOOLS = {
    "scanner": "Scan website for common paths",
    "proxy": "Scrape and validate public proxies",
    "lookup": "IP/Domain geolocation lookup",
    "shell": "Generate a sandbox-safe reverse shell"
}

def main():
    parser = argparse.ArgumentParser(description="MASAN Toolkit CLI", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("tool", choices=TOOLS.keys(), help="Tool to run:\n  " + "\n  ".join(f"{k} - {v}" for k, v in TOOLS.items()))
    parser.add_argument("--target", help="Target domain/IP (if required)")
    parser.add_argument("--port", type=int, help="Port for reverse shell")
    parser.add_argument("--output", help="Output filename for generated payload")
    args = parser.parse_args()

    if args.tool == "scanner":
        if not args.target:
            sys.exit("[!] You must provide --target for scanner")
        scanner.scan_target(args.target)

    elif args.tool == "proxy":
        proxy_scraper.main()

    elif args.tool == "lookup":
        if not args.target:
            sys.exit("[!] You must provide --target for lookup")
        ip_lookup.lookup_ip(args.target)

    elif args.tool == "shell":
        if not args.target or not args.port:
            sys.exit("[!] You must provide --target (IP) and --port for reverse shell")
        reverse_shell.generate_reverse_shell(args.target, args.port, args.output or "reverse_shell.py")

if __name__ == "__main__":
    main()