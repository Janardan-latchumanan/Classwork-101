import dropbox 

class TransferData:
	def __init__(self, access_token):
		self.access_token = access_token

	def upload_file(self , file_from , file_to):
		dbx = dropbox.Dropbox(self.access_token)
		f = open(file_from , 'rb')
		dbx.files_upload(f.read() , file_to) 

def main():
	access_token = "sl.AyKFxzTc16G_rHNcJuvdYR3q8yKO3lKoqO8o8IyivD3ncdSWY7mnrSZQRjo4YUAGcxkFiGYHOPM_MK5IiXOt_YZH1PWNxJkYyd3YGFoOKeGSd8pEv1Z8T_tOtKYYASjQ1v0th1E"
	transferData  = TransferData(access_token)

	file_from = input("Enter your file path to transfer : ")
	file_to = input("Enter you Destination path : ")
	transferData.upload_file(file_from , file_to)

main()	
