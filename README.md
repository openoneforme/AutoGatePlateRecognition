# AutoGatePlateRecognition

Powered by casaIoT Sdn. Bhd.

![cover](https://github.com/openoneforme/AutoGatePlateRecognition/blob/main/image/cover.png)

Team Members:
Name                                | Matrics Number          | Role                    |             
----------------------------------  | ----------------------- | ----------------------- |
Jasni Jazali Bin Mohd Zamri         | B031910077              | Project Manager         |
Mukheish Rao A/L M.Apparao          | B031910099              | Project Scheduler       |
Wan Ali Bin Mohamad Pauzi           | B031910397              | Financial Analyst       |
Farabi Tasnim Ahmed                 | B031910456              | Quality Manager         |  

## Project Definition

Project Title: Auto Gate Plate Recognition

Objectives: 

1.  To helps owner open their house gate without going out from car
2.  To improve house security
3.  To record all the vehicle that are at in front of the gate


## Project Planning
<h2>Gantt Chart</h2>

![GanttChart](https://github.com/openoneforme/AutoGatePlateRecognition/blob/main/image/GanttChart.JPG)


<h2>Responsibility Assignment Matrices (RAM)</h2>

![RAM](https://github.com/openoneforme/AutoGatePlateRecognition/blob/main/image/RAM.JPG)

<h2>Roles & Resposibility</h2>

<br>

| Name                                     | Roles                   |
| ---------------------------------------- | ----------------------- |
| Jasni Jazali Bin Mohd Zamri              | Project Manager         |
| Mukheish Rao A/L M.Apparao               | Project Scheduler       |
| Wan Ali Bin Mohamad Pauzi                | Financial Analyst       |
| Farabi Tasnim Ahmed                      | Quality Manager         |

<br>
<h2>NPV</h2>

![NPV](https://github.com/openoneforme/AutoGatePlateRecognition/blob/main/image/NPV.JPG)


## Project Implementation

<h2>Cost Estimation</h2>

![Cost Estimation](https://github.com/openoneforme/AutoGatePlateRecognition/blob/main/image/Cost%20Estimation.JPG)

<h2>Time Management Gantt Chart</h2>

![Time Management](https://github.com/openoneforme/AutoGatePlateRecognition/blob/main/image/Time%20Management.JPG)


## Project Execution

Flowchart:

![FLowchatAIPM drawio](https://github.com/openoneforme/AutoGatePlateRecognition/blob/main/image/Flowchart.png)

Below are some of the code snipets attached:

First we need to do some pre-processing on the image of the car, so the number plate is more readable.
![Screenshot (339)](https://github.com/openoneforme/AutoGatePlateRecognition/blob/main/image/code%20(3).png)

Then we need to crop the number plate part of the image, and then using easOCR we read the part of the image that we have cut, 
and converted it into text and store it into an array.

![Screenshot (340)](https://github.com/openoneforme/AutoGatePlateRecognition/blob/main/image/code.png)

Then we display the number plate that we have read, and run a simulation whehter our gate opens or remains closed.
![Screenshot (342)](https://github.com/openoneforme/AutoGatePlateRecognition/blob/main/image/code%20(2).png)

Project Result:

![Screenshot (347)](https://user-images.githubusercontent.com/55405230/150632899-649f851b-1395-4002-b761-b541080b5d42.png)

![Screenshot (344)](https://user-images.githubusercontent.com/55405230/150632851-20277dac-7890-41e8-9394-8ed97d2ddb15.png)



## Project Closure

Closing Checklist

:white_check_mark: [Sign Off](https://github.com/openoneforme/AutoGatePlateRecognition/blob/main/documentation/Sign%20Off.pdf)

:white_check_mark: [Lesson Learned](https://github.com/openoneforme/AutoGatePlateRecognition/blob/main/documentation/Lesson%20Learned.pdf)

:white_check_mark: [Final Project Report](https://github.com/openoneforme/AutoGatePlateRecognition/blob/main/README.md)

:white_check_mark: [Closing Contract](https://github.com/openoneforme/AutoGatePlateRecognition/blob/main/documentation/Close%20Contract.pdf)

## Project Presentation

Presentation Video
* Click the video below to watch our live recorded presentation

[![Presentation](https://github.com/openoneforme/AutoGatePlateRecognition/blob/main/image/Thumbnail.JPG)](https://www.youtube.com/watch?v=ZpWf4k8uwMQ "AutoGatePlateRecognition Project Presentation")

Demonstration Video
* Click the video below to watch our demonstration video

[![Demo](https://github.com/openoneforme/AutoGatePlateRecognition/blob/main/image/Thumbnail2.JPG)](https://www.youtube.com/watch?v=iZLoIcoBv9A "AutoGatePlateRecognition Project Demonstration")
