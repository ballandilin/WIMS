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
from package import bdConnection
# import cv2



class App():
	def __init__(self, img1, img2):


		# connection a la base donnée
		self.urlDb = "mongodb+srv://iutUser:IG0Yo4sdvxvK5sEO@cluster0.ykzqu.mongodb.net/PROJETIUT?retryWrites=true&w=majority"
		self.client = bdConnection.MongoConnect(self.urlDb)
	

		self.predictor_file = "./shape_predictor_68_face_landmarks.dat"
		self.face_rec_model_path = "./dlib_face_recognition_resnet_model_v1.dat"


		self.detector = dlib.get_frontal_face_detector()
		self.sp = dlib.shape_predictor(self.predictor_file)
		self.facerec = dlib.face_recognition_model_v1(self.face_rec_model_path)

		self.img1 = img1
		self.img2 = self.convertBase64ToJpg(img2)


		self.vec2 = self.getVectorImg(self.img2)

		self.people = []
		self.threads = []

		self.distances = {}
		self.distances['people'] = []
		self.distancesList = []




	def begin(self):
		"""

		Function: begin

		Summary: begin the process

		Examples:  

		Attributes: 

			@param (self): 


		Returns:  

		"""
		ret = None
		if self.isThereFace(self.img2):

			self._loadDb()

			if self.distances['people']:
				self.get_saved_data()
			else:
				self.run(self.img1)

			ret = self.get_comp_name(self.distancesList)
		else:
			ret = "face not found"

		return ret



	def convertBase64ToJpg(self, img):
		"""

		Function: convertBase64ToJpg

		Summary: Fucntion that allows to convert a either a png encoded in base64 or a jpg encoded in base64 in jpg 

		Examples:  

		Attributes: 

			@param (self): 


		Returns:  

		"""
		if ("png" in img):
			img = img[22::]
		else:
			img = img[23::]


		str.encode(img)
		imgData = base64.b64decode(img)

		image = PIL.Image.open(BytesIO(imgData))

		img = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
		PIL.save('./static/out.jpg', 'JPEG')
		path = './static/out.jpg'
		return path




	def isThereFace(self, img):
		"""

		Function: isThereFace

		Summary: test if there is face in the picture

		Examples:  

		Attributes: 

			@param (self): 

			@param (img): the picture that need to be test 


		Returns:  

		"""
		img = self.optimizeImg(img, 500)
		dets = self.detector(img, 1)
		return len(dets)


	def _save(self, dico):
		"""

		Function: _save

		Summary: save 128d vector for each picture in a json file

		Examples:  

		Attributes: 

			@param (self): 

			@param (dico): 

		Returns:  

		"""
		self.client.sendData(self.distances['people'])

	def _saveDb(self, dico):
		"""

		Function: _saveDb

		Summary: save 128d vector for each picture in a json file

		Examples: 

		Attributes: 

			@param (self):

			@param (dico):Dict that contains distances for each people

		Returns: 

	"""
		self.client.sendData(self.distances['people'])


	def _load(self):
		"""

		Function: _load

		Summary: load data from json file

		Attributes: 

			@param (self):

		Returns: 

		"""
		try:
			with open('./data.json') as outfile:
				data = json.load(outfile)
				self.distances.update(data)
		except Exception as e:
			print(e)



	def _loadDb(self):
		"""

			Function: _loadDb

			Summary: load data from mondoDb database

			Attributes: 

				@param (self):

			Returns:

		"""
		try:

			data = self.client.getData()
			j = {}

			for d in data:
				j[d['name']] = d['data']


			self.distances['people'].append(j)
		except Exception as e:
			print(e)




	def run(self, directory):
		"""

		Function: run

		Summary: 

		Examples: function that init thread to process all the picture in the subdirectory which is contains in the directory

		Attributes: 

			@param (self):

			@param (directory): directory that contain subdirectory with celebrities's pictures

		Returns:  

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

		Examples:  

		Attributes: 

			@param (self): 

			@param (distance): distance between two faces

		Returns:  

		"""
		return sum(distance) / len(distance)



	def compute(self, dir):
		"""

		Function: compute

		Summary: get the euclidian distance with each celebrities's picture

		Examples:  

		Attributes: 

			@param (self): 

			@param (dir): directory for people img

		Returns:  

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

		Examples:  

		Attributes: 

			@param (self): 

		Returns:  

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

		Examples:  

		Attributes: 

			@param (self): 

			@param (path): path to the directory that contains the img which need to be processed

		Returns:  

		"""

		vecList = []

		dico = {}
		name = self.people[len(self.people) - 1]
		dico[name] = []

		for f in glob.glob(os.path.join(path, "*.jpg")):
			ret = []
			file = str(os.path.basename(f).split(".jpg")[0])
			result = self.getVectorImg(f, True)
			if result:
				# if len(dico[name]):
				# 	dico[name][0].append(result[0].tolist())
				# dico[name].append(result[0].tolist())
				dico[name].append({file : result[0].tolist()})
				vecList.append(result)

		# self._save(dico)
		self._saveDb(dico)
		return vecList


	def optimizeImg(self, img, thres):
		"""

		Function: optimizeImg

		Summary: Allows to optimize the img by shrink it

		Examples:  

		Attributes: 

			@param (self): 

			@param (img): img that need to be optimize

		Returns:  

		"""
		img = dlib.load_rgb_image(img)

		if max(np.array(img).shape) > thres:
			pil_img = PIL.Image.fromarray(img)
			pil_img.thumbnail((thres, thres), PIL.Image.LANCZOS)
			img = np.array(pil_img)

		return np.array(img)



	def getVectorImg(self, img, FullPath=False):
		"""

		Function: getVectorImg

		Summary: get 128D vector for picture in parameter

		Examples:  

		Attributes: 

			@param (self): 

			@param (img): Img that need to be processed

			@param (FullPath) default=False:  False if we pass just the directory name

		Returns:  

		"""
		vecList = []

		img = self.optimizeImg(img, 1000)

		dets = self.detector(img, 1)

		for k, d in enumerate(dets):

			shape = self.sp(img, d)

			return [np.array(self.facerec.compute_face_descriptor(img, shape))]




	def get_distance(self, img1, img2):
		"""

		Function: get_distance

		Summary: get the euclidian distance between a list of processed picture and the user's picture

		Examples:  

		Attributes: 

			@param (self): 

			@param (img1): img to compare with a bunch of other img

			@param (img2): list of img to compare with

		Returns:  

		"""
		return [np.linalg.norm(i - img2[0], axis=0) for i in img1]


	def compare_face(self, img1, img2, tol=0.6):
		"""

		Function: compare_face

		Summary: compare two face

		Examples:  

		Attributes: 

			@param (self): 

			@param (img1): img to compare with a bunch of other img

			@param (img2): list of img to compare with

			@param (tol): tolerance to compare 2 img

		Returns:  

		"""
		return list(bool(i <= tol) for i in self.get_distance(img1, img2))


	def get_comp_name(self, distanceList):
		"""

		Function: get_comp_name

		Summary: return comparaison between two face

		Examples:  

		Attributes: 

			@param (self): 

			@param (distanceList): return the list with each distance between each person 

		Returns:  

		"""
		sosie = 0
		name = ""

		if distanceList:
			sosie = distanceList.index(min(distanceList))
			name = self.people[sosie]

		return name






if __name__ == "__main__":
	

	img1 = "./img/imgSet/"

	# img2 = "\\img\\imgComp\\3.jpg"
	# start_time = time.time()

	for lines in sys.stdin:
		data = lines

	app = App(img1, data)
	app.begin()
	# print(time.time() - start_time)
