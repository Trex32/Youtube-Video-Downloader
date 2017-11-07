from YoutubeDownloader.Utils.Download import Download
from YoutubeDownloader.Utils.Helper import create_directory_if_not_exist
import pafy
import os
import time

class VideoDownloader:

    def __init__(self, url = None, output_directory = None):
        self._url = url
        self._output_dir = output_directory
        self._pafy_obj = None
        self._stream = None

        self._id = None
        self._title = None
        self._duration = None
        self._length = None
        self._author = None
        self._download_link = None
        self._output_filename = None

    @property
    def pafy_obj(self):
        if self._pafy_obj == None:
            self._pafy_obj = pafy.new(self._url)
        return self._pafy_obj

    @property
    def stream(self):
        if self._stream == None:
            self._stream = self.pafy_obj.getbest()
        return self._stream

    def fetch(self):
        self._id = self.pafy_obj.videoid
        self._title = self.pafy_obj.title
        self._length = self.pafy_obj.length
        self._duration = self.pafy_obj.duration
        self._author = self.pafy_obj.author
        self._download_link = self.stream.url
        self._download_extension = self.stream.extension


    @property
    def save_path(self):
        if self._output_filename == None:
            self._output_filename = os.path.join(self._output_dir, self._title + "." + self._download_extension)
        return os.path.abspath(self._output_filename)



    def download(self):
        dirname = os.path.abspath(os.path.dirname(self.save_path))
        create_directory_if_not_exist(dirname)
        try:
            print("Downloading: {}".format(self._title))
            download_obj = Download(self._download_link, self.save_path)
            download_obj.run()
            #self.stream.download(self.save_path)
            return True
        except Exception as e:
            print(e)
            return False

    def run(self):
        self.fetch()
        self.download()



if __name__ == '__main__':
    video_link = 'https://www.youtube.com/watch?v=qLpCld4cdtk'
    obj = VideoDownloader(video_link)
    obj.run()