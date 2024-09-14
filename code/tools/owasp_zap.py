import time
import zapv2

def scan_with_zap(target_url):
    try:
        zap = zapv2.ZAPv2(apikey='your_api_key', proxies={'http': 'http://localhost:8080', 'https': 'http://localhost:8080'})

        # Open URL
        try:
            zap.urlopen(target_url)  # Removed 'verify=False' to avoid conflict
        except Exception as e:
            print(f"Failed to open URL: {e}")
            return []

        time.sleep(2)  # Wait for ZAP to fully load the page

        # Spider the site
        try:
            print(f"Starting spider scan on {target_url}...")
            zap.spider.scan(target_url)
        except Exception as e:
            print(f"Failed to start spider scan: {e}")
            return []

        print("Waiting for spider scan to complete...")
        while int(zap.spider.status()) < 100:
            time.sleep(2)

        # Active scan
        try:
            print(f"Starting active scan on {target_url}...")
            zap.ascan.scan(target_url)
        except Exception as e:
            print(f"Failed to start active scan: {e}")
            return []

        print("Waiting for active scan to complete...")
        while int(zap.ascan.status()) < 100:
            time.sleep(5)

        # Fetch alerts
        try:
            alerts = zap.core.alerts()
            print(f"Found {len(alerts)} alerts")
            return alerts
        except Exception as e:
            print(f"Failed to fetch alerts: {e}")
            return []

    except Exception as e:
        print(f"An error occurred: {e}")
        return []
