import aiofiles
import os

async def save_file(file, upload_dir):
    file_path = os.path.join(upload_dir, file.filename)
    async with aiofiles.open(file_path, "wb") as out_file:
        content = await file.read()
        await out_file.write(content)
    return file_path
