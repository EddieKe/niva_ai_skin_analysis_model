import React, { useState, useRef } from 'react';
import { UploadImage } from '../controllers/actions'
import { useNavigate } from 'react-router-dom';

import WebcamCapture from './Components/webCam'

// MUI
import Grid from '@mui/material/Grid';
import Container from '@mui/material/Container';
import PhotoCameraIcon from '@mui/icons-material/PhotoCamera';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

function ImageInput() {
    const [landingPage, setLandingPage] = useState(true)
    const [showCamera, setShowCamera] = useState(false)
    const [imageSrc, setImageSrc] = useState(null)
    const fileInputRef = useRef(null)
    const navigate = useNavigate();
    
    if(imageSrc !== null) {
        console.log("we got an image")
        UploadImage(imageSrc, navigate)
    }

    const handleFileUpload = (event) => {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                setImageSrc(e.target.result);
            };
            reader.readAsDataURL(file);
        }
    };

    const triggerFileInput = () => {
        fileInputRef.current?.click();
    };

    const handleTakePhoto = () => {
        setLandingPage(false);
        setShowCamera(true);
    };

    const handleBackToLanding = () => {
        setLandingPage(true);
        setShowCamera(false);
    };

    return (
        <>
            <Container maxWidth="xs" sx={{padding: 0}} alignitems="center">
                <Grid container justify="center" sx={{maxHeight:"100vh"}} spacing={1}>
                    {landingPage ? 
                        <Grid item xs={8} sx={{margin:"35vh auto"}} textAlign="center">
                            <PhotoCameraIcon sx={{fontSize:"4em", marginBottom: "2vh"}}/>
                            <Typography variant="h6" sx={{marginBottom: "3vh"}}>
                                Add your photo
                            </Typography>
                            
                            <Button 
                                onClick={handleTakePhoto} 
                                variant="contained"
                                fullWidth
                                startIcon={<PhotoCameraIcon />}
                                sx={{marginBottom: "2vh"}}>
                                Take a photo
                            </Button>
                            
                            <Button 
                                onClick={triggerFileInput} 
                                variant="outlined"
                                fullWidth
                                startIcon={<CloudUploadIcon />}>
                                Upload from gallery
                            </Button>
                            
                            {/* Hidden file input */}
                            <input
                                type="file"
                                accept="image/*"
                                onChange={handleFileUpload}
                                ref={fileInputRef}
                                style={{ display: 'none' }}
                            />
                        </Grid>
                        :
                        <Grid item xs={12}>
                            {showCamera && (
                                <>
                                    <Button 
                                        onClick={handleBackToLanding}
                                        variant="text"
                                        sx={{margin: "1vh"}}>
                                        ← Back
                                    </Button>
                                    <WebcamCapture setImageSrc={setImageSrc}/>
                                </>
                            )}
                        </Grid>
                    }
                </Grid>   
            </Container>
        </>
    )
}

export default ImageInput