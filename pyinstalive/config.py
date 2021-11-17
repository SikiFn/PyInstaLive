import os

class Config:
    parser_object = None
    config_path = os.path.join(os.getcwd(), "pyinstalive.ini")
    username = None
    password = None
    download_path = os.getcwd()
    show_session_expires = True
    download_comments = True
    clear_temp_files = False
    cmd_on_started = None
    cmd_on_ended = None
    ffmpeg_path = None
    log_to_file = False
    no_assemble = False
    use_locks = True