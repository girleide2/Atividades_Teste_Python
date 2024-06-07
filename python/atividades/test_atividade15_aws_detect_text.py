import pytest
from atividade15_aws_detect_text import detect_text_resource

@pytest.fixture
def sample_image_path():
    return 'img-to-aws.jpg'

def test_detect_text_resource(sample_image_path):
    response = detect_text_resource(sample_image_path)
    assert 'TextDetections' in response
    assert len(response['TextDetections']) > 0

def test_detect_text_resource_invalid_path():
    with pytest.raises(FileNotFoundError):
        detect_text_resource('invalid_path.jpg')
        
if __name__ == "__main__":
    pytest.main(["-s", "-x", "test_atividade15_aws_detect_text.py", "-vv"])

