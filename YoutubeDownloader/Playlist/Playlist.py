from YoutubeDownloader.Video.Video import VideoDownloader
import os
import pafy
import threading
import time

class PlaylistDownloader:
    def __init__(self, url, output_dir, batch_size = 1):
        self._url = url
        self._output_dir = output_dir
        self._pafy_obj = None
        self.batch_size = batch_size

    @property
    def pafy_obj(self):
        if self._pafy_obj == None:
            self._pafy_obj = pafy.get_playlist(self._url)
        return self._pafy_obj

    @property
    def video(self):
        return self.pafy_obj['items']

    @property
    def title(self):
        return self.pafy_obj['title']

    @property
    def video_count(self):
        return len(self.pafy_obj['items'])


    def download(self, item_number):
        video_obj = VideoDownloader()
        video_obj._pafy_obj = self.video[item_number]['pafy']
        video_obj.fetch()
        video_obj._output_filename = os.path.join(
            self._output_dir, self.title, "{}.{}".format(str(item_number+1),video_obj._download_extension))
        video_obj.download()

    def run(self):
        starting_thread_count = threading.active_count()
        for i in range(self.video_count):
            # self.download(i)
            while threading.active_count() > starting_thread_count + self.batch_size:
                time.sleep(0.05)
            threading.Thread(target=self.download, args=(i,)).start()
        while threading.active_count() != starting_thread_count:
            time.sleep(0.05)