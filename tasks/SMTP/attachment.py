import os
import mimetypes
import utils


class Attachment:
    def __init__(self, filename: str):
        fname, ext = os.path.splitext(filename)
        mimetypes.init()
        mime = mimetypes.types_map[ext]
        name = filename.split("/")[-1]
        base64_filename = f"=?UTF-8?B?{utils.get_base64string(name)}?="
        base64_attachment = utils.get_file_content(filename)
        self.content = ""
        self.content += f"Content-Type: {mime}; name=\"{base64_filename}\"\n"
        self.content += f"Content-Disposition: attachment; filename=\"{base64_filename}\"\n"
        self.content += f"Content-Transfer-Encoding: base64\n\n"
        self.content += base64_attachment

