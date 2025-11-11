import siemens_tia_scripting as ts
import os
from pathlib import Path
from datetime import datetime

# Config
project_file_path = Path(r"C:\Users\z0056j1u\Documents\Automation\ReactorProject\Reactor_V20\Reactor_V20.ap20")
print(f"Opening project at path{project_file_path}")
archived_project_output_path = Path.joinpath(Path.cwd(), Path("build/"))
print(archived_project_output_path)


# Open TIA portal
print(f"Opening portal without UI at file path: {project_file_path}")
portal = ts.open_portal(ts.Enums.PortalMode.WithoutGraphicalUserInterface, version="20.0" )

# Open project
project = portal.open_project(project_file_path=str(project_file_path), server_project_view=False)

# Ensure output folder is created
archived_project_output_path.mkdir(parents=True, exist_ok=True)

# Create archive of project
current_date = datetime.now()
date_as_str = current_date.strftime("%m_%d_%Y__%H_%M_%S")
archived_project_name = project_file_path.stem + " " + date_as_str

# Create archive
project.archive(target_directory_path=str(archived_project_output_path), archive_name=archived_project_name, delete_existing_archive=False)