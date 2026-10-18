import os


def get_files_info(working_directory: str, directory: str = ".") -> str:

    try:
        directory_label = f"'{directory}'" if directory != "." else "current directory"
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = (
            os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        )

        if not valid_target_dir:
            print(f"\nresults for '{directory_label}' directory:\n")
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            print(f"\nresults for '{directory_label}' directory:\n")
            return f'Error: "{directory}" is not a directory'

        if valid_target_dir:
            print(f"\nresults for '{directory_label}' directory:\n")
            for file in os.listdir(target_dir):
                file_path = os.path.join(target_dir, file)
                file_size = os.path.getsize(file_path)
                is_directory = os.path.isdir(file_path)
                print (f"- {file}: file_size={file_size} bytes, is_dir={is_directory}")
            return f'Success: "{directory_label}" is within the working directory'

    except Exception as e:
        return f"{e}"
