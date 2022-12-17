class Individual:
	all = []
	def __init__(self, genotype,name = None):

		self.__name = name
		self.__genotype = genotype
		
		if self.__name == None:
			self.__name = 'Indiv' + str(len(Individual.all)+1)
		
		if not isinstance(self.__genotype,(str)):
		    raise TypeError('genotype attribute must be a string!')
		elif self.__genotype not in ['AA','Ai','BB','Bi','AB','ii']:
		    raise ValueError('Invalid genotype!')

		Individual.all.append(self)

	def _name(self):
		return self.__name
	

	def _genotype(self):
		return self.__genotype
	

	def _blood_type(self):
		if self.__genotype == 'AA' or self.__genotype == 'Ai':
			return 'A'
		elif self.__genotype == 'BB' or self.__genotype == 'Bi':
			return 'B'
		elif self._genotype == 'AB':
		    return 'AB'
		else: 
		    return 'O'


	def _agglutinogens(self):
		if self.__genotype == 'AA' or self.__genotype == 'Ai':
			return 'A'
		elif self.__genotype == 'BB' or self.__genotype == 'Bi':
			return 'B'
		elif self.__genotype == 'AB':
			return 'A and B'
		else: return 'no agglutinogens'


	def _agglutinins(self):
		if self.__genotype == 'AA' or self.__genotype == 'Ai':
			return 'B'
		elif self.__genotype == 'BB' or self.__genotype == 'Bi':
			return 'A'
		elif self.__genotype == 'AB':
			return 'no agglutinins'
		else: return 'A and B'
		


	def offsprings_genotypes(self,indiv):
		if not isinstance(indiv,(Individual)):	
		    raise TypeError('indiveter must be of Individual class type!')
		
		if self.__genotype == 'AA' and indiv.__genotype == 'AA':
			return 'AA'
		elif self.__genotype == 'BB' and indiv.__genotype == 'BB':
			return 'BB'
		elif self.__genotype == 'AA' and indiv.__genotype == 'BB':
			return 'AB'
		elif self.__genotype == 'Ai' and indiv.__genotype == 'Ai':
			return 'AA','Ai'
		elif self.__genotype == 'Bi' and indiv.__genotype == 'Bi':
			return 'BB','Bi'
		elif self.__genotype == 'Ai' and indiv.__genotype == 'BB':
			return 'AB','Bi'
		elif self.__genotype == 'BB' and indiv.__genotype == 'Ai':
			return 'AB','Bi'
		elif self.__genotype == 'AA' and indiv.__genotype == 'Bi':
			return 'AB','Ai'
		elif self.__genotype == 'Bi' and indiv.__genotype == 'AA':
			return 'AB','Ai'
		elif self.__genotype == 'Ai' and indiv.__genotype == 'Bi':
			return 'AB','Ai','Bi','ii'
		elif self.__genotype == 'Bi' and indiv.__genotype == 'Ai':
			return 'AB','Ai','Bi','ii'
		elif self.__genotype == 'AA' and indiv.__genotype == 'ii':
			return 'Ai'
		elif self.__genotype == 'ii' and indiv.__genotype == 'AA':
			return 'Ai'
		elif self.__genotype == 'Ai' and indiv.__genotype == 'ii':
			return 'Ai','ii'
		elif self.__genotype == 'ii' and indiv.__genotype == 'Ai':
			return 'Ai','ii'
		elif self.__genotype == 'BB' and indiv.__genotype == 'ii':
			return 'Bi'
		elif self.__genotype == 'ii' and indiv.__genotype == 'BB':
			return 'Bi'
		elif self.__genotype == 'Bi' and indiv.__genotype == 'ii':
			return 'Bi','ii'
		elif self.__genotype == 'ii' and indiv.__genotype == 'Bi':
			return 'Bi','ii'
		elif self.__genotype == 'ii' and indiv.__genotype == 'ii':
			return 'ii'


	def offsprings_blood_types(self,indiv):
		if not isinstance(indiv,(Individual)):
		    raise TypeError('indiveter must be of Individual class type!')
		    
		if self.__genotype == 'AA' and indiv._genotype() == 'AA':
			return 'A'
		elif self.__genotype == 'BB' and indiv._genotype() == 'BB':
			return 'B'
		elif self.__genotype == 'AA' and indiv._genotype() == 'BB':
			return 'AB'
		elif self.__genotype == 'Ai' and indiv._genotype() == 'Ai':
			return 'A'
		elif self.__genotype == 'Bi' and indiv._genotype() == 'Bi':
			return 'B'
		elif self.__genotype == 'Ai' and indiv._genotype() == 'BB':
			return 'AB','B'
		elif self.__genotype == 'BB' and indiv._genotype() == 'Ai':
			return 'AB','B'
		elif self.__genotype == 'AA' and indiv._genotype() == 'Bi':
			return 'AB','A'
		elif self.__genotype == 'Bi' and indiv._genotype() == 'AA':
			return 'AB','A'
		elif self.__genotype == 'Ai' and indiv._genotype() == 'Bi':
			return 'AB','A','B','O'
		elif self.__genotype == 'Bi' and indiv._genotype() == 'Ai':
			return 'AB','A','B','O'
		elif self.__genotype == 'AA' and indiv._genotype() == 'ii':
			return 'A'
		elif self.__genotype == 'ii' and indiv._genotype() == 'AA':
			return 'A'
		elif self.__genotype == 'Ai' and indiv._genotype() == 'ii':
			return 'A','O'
		elif self.__genotype == 'ii' and indiv._genotype() == 'Ai':
			return 'A','O'
		elif self.__genotype == 'BB' and indiv._genotype() == 'ii':
			return 'B'
		elif self.__genotype == 'ii' and indiv._genotype() == 'BB':
			return 'B'
		elif self.__genotype == 'Bi' and indiv._genotype() == 'ii':
			return 'B','O'
		elif self.__genotype == 'ii' and indiv._genotype() == 'Bi':
			return 'B','O'
		elif self.__genotype == 'ii' and indiv._genotype() == 'ii':
			return 'O'
			
			
	def can_receive(self,indiv):
		if not isinstance(indiv,(Individual)):
			raise TypeError('indiveter must be of Individual class Type')

		if self._blood_type() == 'A' and indiv._blood_type  == 'A' or indiv._blood_type() == 'O':
			return True

		elif self._blood_type() == 'B' and indiv._blood_type() in ['B','O']:
			return True

		elif self._blood_type() == 'AB' and indiv._blood_type() in ['A','B','AB','O']:
			return True

		elif self._blood_type() == 'O' and indiv._blood_type() == 'O':
			return True
		else:
			return False
		
	def can_donate(self,indiv):
		if not isinstance(indiv,(Individual)):
			raise TypeError('indiveter must be of Individual class Type')
			
		if self._blood_type() == 'A' and indiv._blood_type() in ['A','AB']:
			return True

		elif self._blood_type() == 'B' and indiv._blood_type() in ['B','AB']:
			return True

		elif self._blood_type() == 'AB' and indiv._blood_type() == 'AB':
			return True

		elif self._blood_type() == 'O':
			return True
		else:
			return False


	def __repr__(self):
		return f"Individual('{self.__name}'),('{self.__genotype}')"

