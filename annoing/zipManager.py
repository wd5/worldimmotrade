# Simple zip helper
# Usage:
# zip = ZipManager()
# zip.read_file("full_path_to_zip_file")
# zip.extract("full_path_to_extract_with_ending_slah")#

import os
import zipfile

class ZipManager:

	def read_file(self, path):
		self.file = zipfile.ZipFile(path, "r")

	def extract(self, path):
		if not os.path.exists(path):
			os.mkdir(path)

		for name in self.file.namelist():
			self._save_file(path + name, self.file.read(name))

	def _save_file(self,path,data):
		file = open(path, 'w')
		file.write(data)
		file.close()
