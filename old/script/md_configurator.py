
assets_path = "C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets"


def simple_automate():
    # clear console window
    mdsa.clear_console()

    #initialize mdsa module
    mdsa.initialize()

    #set exporting option
    mdsa.set_open_option("cm", 30)

    #set importing option
    mdsa.set_save_option("mm", 30, False)

    #designate the folder where the files will be stored and file extension setting
    mdsa.set_save_folder_path(f"{assets_path}\\", "out")


    #set Alembic Format True = Ogawa, False = hdf5. Default is hdf5. (This function is only valid when exporting alembic file.)
    mdsa.set_alembic_format_type(True)

    mdsa.set_avatar_file_path(f"{assets_path}\\Avatar\\Avatar\\Female_V2\\FV2_Feifei.avt")

    mdsa.set_animation_file_path(f"{assets_path}\\Avatar\\Avatar\\Female_V2\\Pose\\FV2_03_Attention.pos")

    mdsa.set_garment_file_path(f"{assets_path}\\Garment\\Tshirt.zpac")

    #Set simulation option.
    mdsa.set_simulation_options(0, 0, 5000)


    #set auto save option. True is save with Zprj File and Image File.
    mdsa.set_auto_save(True)

    #If you finish setting file paths and options. You must call process function.
    mdsa.process()