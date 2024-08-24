import re
import requests


def url_checker(url):
    
    if not re.match(r'^https?://', url):
        raise ValueError("Invalid URL. Please use a valid http or https URL.")

def shorten_url(long_url):
    rebrandly_api_key = '139afb00000000000000000000000'  # Replace with your Rebrandly API key
    headers = {
        'apikey': rebrandly_api_key,
        'Content-Type': 'application/json'
    }
    data = {
        'destination': long_url,
        'domain': {'fullName': 'rebrand.ly'}
    }
    response = requests.post('https://api.rebrandly.com/v1/links', json=data, headers=headers)
    response.raise_for_status()
    short_url = response.json().get('shortUrl')
    return short_url

# main script
def main():
    print("\n███╗   ███╗ ██████╗ ██████╗ ██████╗ ██╗  ██╗ ██████╗ ███████╗")
    print("████╗ ████║██╔═══██╗██╔══██╗██╔══██╗██║  ██║██╔═══██╗██╔════╝")
    print("██╔████╔██║██║   ██║██████╔╝██████╔╝███████║██║   ██║███████╗")
    print("██║╚██╔╝██║██║   ██║██╔══██╗██╔═══╝ ██╔══██║██║   ██║╚════██║")
    print("██║ ╚═╝ ██║╚██████╔╝██║  ██║██║     ██║  ██║╚██████╔╝███████║")
    print("╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝")
    print("                                                            ")
    print("    ━━━━━━━━━━━━━━━━━")
    print("      Python URL Morphing")
    print("    ━━━━━━━━━━━━━━━━━")
    print("        Refactor by: ATX")
    print("")


    
    phish = input("Paste Phishing URL here with http or https: ")
    url_checker(phish)

    
    print("Hold on, shortening Phishing URL...")
    short_url = shorten_url(phish)
    shorter = short_url.replace('https://', '')
    print(f"\nPhishing URL shortened: \033[32mhttps://{short_url}\033[0m\n")

    
    morph = input('Domain to morph the Phishing URL (with http or https), e.g., https://google.com:')
    url_checker(morph)


    words = input('\nInsert social engineering words (e.g., news-money, deal-bussines-trips):\n'
                  '\033[31mAvoid spaces; use "-" instead.\033[0m\n=> ')


    print("\nGenerating Morph Phishing Link...\n")
    final_url = f"{morph}-{words}@{shorter}"
    print(f"Your Morph Phishing URL:\033[32m {final_url} \033[0m\n")

if __name__ == "__main__":
    main()
