import os
import pycurl


class Download:
    def __init__(self,url, output_filename):
        self._url = url
        self._output_filename = output_filename
        self._started = False
        self._downloaded = False
        self._failed = False

    def download(self):
        with open(os.path.abspath(self._output_filename),'wb') as filecon:
            curl = pycurl.Curl()
            curl.setopt(pycurl.URL, self._url)
            curl.setopt(pycurl.FOLLOWLOCATION, 1)
            curl.setopt(pycurl.MAXREDIRS, 5)
            curl.setopt(pycurl.CONNECTTIMEOUT, 30)
            curl.setopt(pycurl.TIMEOUT, 300)
            curl.setopt(pycurl.NOSIGNAL, 1)
            curl.setopt(pycurl.WRITEDATA, filecon)
            try:
                self._started = True
                curl.perform()
                self._downloaded = True

            except Exception as e:
                self._failed = True
                os.remove(self._output_filename)
                print(e)

    def run(self):
        self.download()


if __name__ == '__main__':
    url = 'http://www.deeplearningbook.org/front_matter.pdf'
    output_filename = 'deep_learning.pdf'
    download_obj = Download(url,output_filename)
    download_obj.run()
