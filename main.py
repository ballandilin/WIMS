import sys
import os
import dlib
import glob
import PIL.Image
import numpy as np
import json
from threading import Thread
import time
import base64
from io import BytesIO
import re
# from bdConnection import MongoConnect



class App():
	def __init__(self, img1, img2):

		# self.url = "mongodb+srv://iutUser:IG0Yo4sdvxvK5sEO@cluster0.ykzqu.mongodb.net/PROJETIUT?retryWrites=true&w=majority"
		# self.client = MongoConnect(self.url)
		


		self.predictor_file = "./shape_predictor_68_face_landmarks.dat"
		self.face_rec_model_path = "./dlib_face_recognition_resnet_model_v1.dat"

		self.detector = dlib.get_frontal_face_detector()
		self.sp = dlib.shape_predictor(self.predictor_file)
		self.facerec = dlib.face_recognition_model_v1(self.face_rec_model_path)

		self.convertImg(img2)

		self.img1 = img1
		self.img2 = './static/out.jpg'


		self.vec2 = self.getVectorImg(self.img2)

		self.people = []
		self.threads = []

		self.distances = {}
		self.distances['people'] = []
		self.distancesList = []

		self._load()

		if self.distances['people']:
			self.get_saved_data()
		else:
			self.run(self.img1)




	def progress(self, ):
		return prog

	def convertImg(self, img):

		save = img[23::]

		str.encode(save)

		im = PIL.Image.open(BytesIO(base64.b64decode(save, '-_')))
		im.save('./static/out.jpg', 'JPEG')


	def begin(self):
		return self.get_comp_name(self.distancesList)

	def _save(self, dico):
		"""

		Function: _save

		Summary: save 128d vector for each picture in a json file

		Examples: InsertHere

		Attributes: 

			@param (self):InsertHere

			@param (dico):InsertHere

		Returns: InsertHere

		"""
		# self.client.sendData(self.distances['people'])
		self.distances['people'].append(dico)
		with open('./data.json', 'w') as outfile:
			json.dump(self.distances, outfile, sort_keys=True, indent=4)



	def _load(self):
		"""

		Function: _load

		Summary: load data from json file

		Attributes: 

			@param (self):InsertHere

		Returns: InsertHere

		"""
		try:
			with open('./data.json') as outfile:
				data = json.load(outfile)
				self.distances.update(data)
		except Exception as e:
			print("erreur : ")
			print(e)




	def run(self, directory):
		"""

		Function: run

		Summary: 

		Examples: function that init thread to process all the picture in the subdirectory which is contains in the directory

		Attributes: 

			@param (self):

			@param (directory): directory that contain subdirectory with celebrities's pictures

		Returns: InsertHere

		"""
		try:
			for subdir in glob.glob(directory + "\\*\\"):
				self.compute(subdir)
				# t = Thread(target=self.compute(subdir))
				# t.start()
				# t.join()
		except Exception as e:
			raise



	def get_average(self, distance):
		"""

		Function: get_average

		Summary: get the average euclidian distance between user's picture and celebrities's picture

		Examples: InsertHere

		Attributes: 

			@param (self):InsertHere

			@param (distance):InsertHere

		Returns: InsertHere

		"""
		return sum(distance) / len(distance)



	def compute(self, dir):
		"""

		Function: compute

		Summary: get the euclidian distance with each celebrities's picture

		Examples: InsertHere

		Attributes: 

			@param (self):InsertHere

			@param (dir):InsertHere

		Returns: InsertHere

		"""
		lname = dir.split('\\')
		name = lname[len(lname) - 2]
		self.people.append(name)
		self.vec1 = self.getVectorList(dir)

		self.distancesList.append(self.get_average(self.get_distance(self.vec1, self.vec2)))


	def get_saved_data(self):
		"""

		Function: get_saved_data

		Summary: format loaded data to be process

		Examples: InsertHere

		Attributes: 

			@param (self):InsertHere

		Returns: InsertHere

		"""
		for people in self.distances['people']:
			for name in people:
				vec1 = []
				self.people.append(name)
				for data in people[name]:
					for key, value in data.items():
						vec1.append(value)
				self.distancesList.append(self.get_average(self.get_distance(vec1, self.vec2)))


	def getVectorList(self, path):
		"""

		Function: getVectorList

		Summary: get the 128d vector for celebrities's picture which is pass in parameters

		Examples: InsertHere

		Attributes: 

			@param (self):InsertHere

			@param (path):InsertHere

		Returns: InsertHere

		"""

		vecList = []

		dico = {}
		name = self.people[len(self.people) - 1]
		dico[name] = []

		for f in glob.glob(os.path.join(path, "*.jpg")):
			# print(f)
			ret = []
			file = str(os.path.basename(f).split(".jpg")[0])
			result = self.getVectorImg(f, True)
			if result:
				# if len(dico[name]):
				# 	dico[name][0].append(result[0].tolist())
				# dico[name].append(result[0].tolist())
				dico[name].append({file : result[0].tolist()})
				vecList.append(result)

		self._save(dico)
		return vecList



	def getVectorImg(self, img, FullPath=False):
		"""

		Function: getVectorImg

		Summary: get 128D vector for picture in parameter

		Examples: InsertHere

		Attributes: 

			@param (self):InsertHere

			@param (img):InsertHere

			@param (FullPath) default=False: InsertHere

		Returns: InsertHere

		"""
		vecList = []

		if FullPath:
			# f = PIL.Image.open(img)
			img = dlib.load_rgb_image(img)
		else:
			# f = PIL.Image.open(os.getcwd() + img)
			img = dlib.load_rgb_image(img)


########   tentative d'optimisation   ##########

		if max(np.array(img).shape) > 1000:
			pil_img = PIL.Image.fromarray(img)
			pil_img.thumbnail((1000, 1000), PIL.Image.LANCZOS)
			img = np.array(pil_img)

			# img = f.convert('RGB')

############################################


		img = np.array(img)

		dets = self.detector(img, 1)

		for k, d in enumerate(dets):

			shape = self.sp(img, d)

			return [np.array(self.facerec.compute_face_descriptor(img, shape))]


	def get_distance(self, img1, img2):
		"""

		Function: get_distance

		Summary: get the euclidian distance between a list of process picture and the user's picture

		Examples: InsertHere

		Attributes: 

			@param (self):InsertHere

			@param (img1):InsertHere

			@param (img2):InsertHere

		Returns: InsertHere

		"""
		return [np.linalg.norm(i - img2[0], axis=0) for i in img1]


	def compare_face(self, img1, img2, tol=0.6):
		return list(bool(i <= tol) for i in self.get_distance(img1, img2))


	def get_comp_name(self, distanceList):
		sosie = 0
		name = ""

		if distanceList:
			sosie = distanceList.index(min(distanceList))
			name = self.people[sosie]

		return name






if __name__ == "__main__":
	

	img1 = "./img/imgSet/"

	# img2 = "\\img\\imgComp\\3.jpg"
	start_time = time.time()


	# # time.sleep(1)

	app = App(img1, "./img/imgComp/0.jpg")
	print(time.time() - start_time)
