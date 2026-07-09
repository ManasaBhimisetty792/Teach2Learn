import uuid
from django.conf import settings
from supabase import create_client

supabase = create_client(
    settings.SUPABASE_URL,
    settings.SUPABASE_KEY
)


def upload_profile_image(image):
    extension = image.name.split(".")[-1]
    filename = f"{uuid.uuid4()}.{extension}"

    file_path = f"profile_images/{filename}"

    image.seek(0)

    supabase.storage.from_("profile-images").upload(
        path=file_path,
        file=image.read(),
        file_options={
            "content-type": image.content_type
        }
    )

    public_url = supabase.storage.from_("profile-images").get_public_url(file_path)

    return public_url