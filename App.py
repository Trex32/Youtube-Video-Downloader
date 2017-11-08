from YoutubeDownloader.Downloader import Downloader
import argparse
import time

parser = argparse.ArgumentParser(description='Youtube Video Downloader')

parser.add_argument('--url',help='URL to Download', type=str, required=True)
parser.add_argument('--save',help='Location to save videos/playlists', type=str)
parser.add_argument('--batch_size', help="No of Concurrent Downloads", type=int, default=4)

args = parser.parse_args()

url = args.url
batch_size = args.batch_size
output_dir = args.save

downloader = Downloader(url=url, output_directory = output_dir, batch_size=batch_size)
downloader.download()
