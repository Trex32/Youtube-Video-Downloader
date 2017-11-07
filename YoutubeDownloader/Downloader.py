

from YoutubeDownloader.Video.Video import VideoDownloader
from YoutubeDownloader.Playlist.Playlist import PlaylistDownloader
from os.path import expanduser
import os

class Downloader:

    def __init__(self, url, output_directory = os.path.join(expanduser('~'),'Videos'), batch_size=4):
        self._url = url
        self._output_dir = output_directory
        self._item_type = None
        self._obj = None
        self.batch_size = batch_size

    @property
    def type(self):
        if self._item_type  != None:
            return self._item_type
        if 'youtube.com/watch' in self._url:
            self._item_type = 'video'
        elif 'youtube.com/playlist' in self._url:
            self._item_type = 'playlist'
        else:
            self._item_type = 'unknown'
        return self._item_type

    @property
    def video(self):
        if self.type == 'video':
            return self._obj
        else:
            raise Exception('NotVideo')

    @property
    def playlist(self):
        if self.type == 'playlist':
            return self._obj
        else:
            raise Exception('NotPlaylist')


    def download(self):
        if self.type == 'video':
            self._obj = VideoDownloader(self._url, self._output_dir)
        elif self.type == 'playlist':
            self._obj = PlaylistDownloader(self._url, self._output_dir, self.batch_size)
        self._obj.run()


if __name__ == '__main__':
    video_url = 'https://www.youtube.com/watch?v=qLpCld4cdtk'
    playlist_url = 'https://www.youtube.com/playlist?list=PLPlACV9U2YPEqciVVc70WFzIuYPvy-fkL'
    obj = Downloader(playlist_url)
    obj.download()
