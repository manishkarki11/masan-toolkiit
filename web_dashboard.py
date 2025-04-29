from flask import Flask, request, render_template_string, send_file
import modules.scanner as scanner
import modules.ip_lookup_tool as ip_lookup
import modules.proxy_scraper as proxy_scraper
import modules.reverse_shell_generator as reverse_shell
...
if __name__ == "__main__":
    app.run(debug=True, port=5000)
