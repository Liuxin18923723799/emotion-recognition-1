Recognizes the facial emotion and overlays emoji, equivalent to the emotion, on the person's face.  

- **Setup the Virtual Environment**
    - Create the virtual environment
        - `python3 -m venv --system-site-packages /path/to/venv`  
    - Activate your virtual-environment
        - Linux: `source /path/to/venv/bin/activate`
        - Windows: `cd /path/to/venv` then `.\Scripts\activate`  
    - Install the requirements
        - `cd root-dir-of-project`
        - `pip install -I -r requirements.txt

- **STEP 1** - generating the facial images 
    1. `cd /to/repo/root/dir`  
    1. run `python3 src/face_capture.py emotion-name num-of-images-to-capture`   
    -- example: `python3 src/face_capture.py cry 200`
    > This will open the cam and all you need to do is give the **cry** emotion from your face.
    - Do this step for all the different emotions in different lighting conditions.
    - I used 300 images for each emotions captured in 3 different light condition (100  each).
    - You can see your images inside the **'images'** folder which will contain different folder for different emotion images.
    
- **STEP 2** - creating the dataset out of it  
    1. run `python3 src/dataset_creator.py`
    - This will **create the ready-to-use dataset** as a python pickled file and save it in the dataset folder.
    
- **STEP 3** - training the model on the dataset and saving it  
    1. run `python3 src/model.py`
    - This will start the model-training and upon the training it will save the tensorflow model in the 'model-checkpoints' folder.  
    - It has the parameters that worked well for me, feel free to change it and explore.  
    
- **STEP 4** - using the trained model to make prediction  
    1. run `python3 src/predictor.py`
    - This will open the cam, and start taking the video feed.
    

