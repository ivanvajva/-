import shutil

path_to_dir = './MODS''

output_filename = 'my-zip'

shutil.make_archive(output_filename, 'zip', path_to_dir)

print('Zip archive of directory created.')
