import os
import random
import string
import zipfile
from django.conf import settings
from dotenv import set_key, find_dotenv


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser


class TemplateUploadAPIView(APIView):
    parser_class = (FileUploadParser,)

    def generate_unique_folder_name(self):
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        folder_name = '3rd-' + random_string
        folder_name = 'user_themes/' + folder_name
        return folder_name

    def post(self, request, *args, **kwargs):
        if 'file' not in request.FILES:
            return Response({'error': 'No file uploaded'}, status=400)

        uploaded_file = request.FILES['file']

        folder_name = self.generate_unique_folder_name()
        folder_path = os.path.join(settings.BASE_DIR, folder_name)

        try:
            os.makedirs(folder_path)

            file_path = os.path.join(folder_path, uploaded_file.name)
            with open(file_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(folder_path)
                # Write folder name to .env
                env_path = find_dotenv()
                set_key(env_path, 'DEFAULT_TEMPLATE_ID', folder_name)

            return Response({'success': True, 'folder_name': folder_name})
        except Exception as e:
            return Response({'error': str(e)}, status=500)


