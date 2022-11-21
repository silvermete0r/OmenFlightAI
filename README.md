# OmenFlight 
<div align="center">
   <img src="https://sun9-west.userapi.com/sun9-13/s/v1/ig2/AQK9TKQ2ldo2BUNW-Sp_ve1xWk-dAHddHVV4msr1e0tqBDPKSjt5L4MzP-l8sv-PUXDvYNEG9gfNB3YJZXWrX8YX.jpg?size=900x900&quality=95&type=album" alt="Logo" width="120" height="120">
   <h3 align="center">OmenFlight AI - the future of birds needs to be solved today!</h3>
</div>
OmenFlight AI is an open-source computer vision program for recognizing birds on video. Our artificial intelligence program will help cameras quickly and accurately recognize birds within the radius of dangerous zones, so that bird scaring devices can prevent cases of birds interacting with deadly zones in time. 

<!-- TABLE OF CONTENTS -->
<details>
  <summary><b>Table of Contents</b></summary>
  <ol>
    <li>
      <a href="#description">Description</a>
      <ul>
        <li><a href="#main-problem">Main Problem</a></li>
        <li><a href="#our-goal">Our Goal</a></li>
        <li><a href="#our-solution">Our Solution</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#dependencies">Dependencies</a></li>
        <li><a href="#installing">Installing</a></li>
        <li><a href="#executing-program">Executing Program</a></li>
      </ul>
    </li>
    <li><a href="#help">Help</a></li>
    <li><a href="#authors">Authors</a></li>
    <li><a href="#version-history">Version History</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## Description

### Main Problem

Birds are an extremely important part of the global ecosystem, the mass death of birds due to human activity can lead to catastrophic results.
* <b>Collision of birds with airplanes</b>: Every year, bird collisions with aircraft cause significant harm to airlines in terms of damage to important components of the aircraft, delays and cancellations of flights. According to the International Civil Aviation Organization (ICAO), there are 34 bird collisions with aircraft per day in the world. The total annual damage caused by the collision of birds with airplanes exceeds $ 1.2 billion, also more than 200 people die, and about 100 aircraft fail every year [<a href="https://www.inventiva.co.in/trends/what-are-bird-strikes-3-potential-risks-to-the-aviation-industry-how-do-pilots-and-airports-tackle-them/">1</a>]. In Kazakhstan, according to Forbes for 2022, more than 100 aircraft collisions with birds have already occurred, which is why flights were often delayed and closed [<a href="https://forbes.kz/process/100_straykov_za_god_pochemu_v_kazahstanskie_samoletyi_vse_chasche_popadayut_ptitsyi/">2</a>].
* <b>Birds colliding with power lines</b>: High-voltage power lines very often intersect with the migration routes of wild birds, so there is a problem of frequent collisions of birds with power lines. “In Kazakhstan, about 58 thousand individuals of birds of prey die annually on high–voltage power lines; 61% of them are birds listed in the Red Book” (Karyakin, 2008) [<a href="https://www.acbk.kz/article/default/view?id=359">3</a>]. 
* <b>Collision of birds with wind farms</b>: Wind farms are definitely one of the best achievements of green energy, but how environmentally friendly is it? Every year, due to the collision of birds with wind farms, more than 300 thousand wild birds die in the world (Eriksson et al., 2014) [<a href="https://abcbirds.org/blog21/wind-turbine-mortality/">4</a>].

### Our Goal

Our main goal is to prevent birds from colliding with important infrastructure facilities.Thus we solve 2 problems at once:
1) We are reducing the mortality rate of birds, which play an important role in local ecosystems.
2) We prevent accidents, breakdowns and delays that occur due to bird collisions with important infrastructure facilities, like airplanes, power lines and wind turbines.

### Our Solution

At the moment, there are quite effective methods of scaring birds in the world, such as: bioacoustic, laser, gas and visual devices for scaring birds. But the problem lies in their timely activation and control of these devices. 

Therefore, as a solution, we are developing a **computer vision program that will be able to detect birds within the radius of dangerous zones and activate bird scaring devices in time.**

Now, our solution works on the basis of an open library of computer vision and algorithms of the Haar cascade. For the first stage of practical application of our program, we plan to use Haar feature algorithms, and we will also experimentally create a program based on LBP (Local Binary Pattern) for fast detection of birds in real time.

Comparing the effectiveness of 2 algorithms on real practical testing, we will come to one solution. Below, you can see a theoretical comparison:

[![Comparison-Haar-LBP][link]](https://medium.com/mindboard/a-deep-learning-solution-to-detect-and-mask-human-faces-in-videos-ad1451e89350)

**Our task is to create a reliable and fast computer vision program capable of detecting birds in the frame with an accuracy of more than 95% in real time (without delays).**

[![Birds-Test-Screen][birds-test]](#)

## Roadmap

- [x] Creating a test model of bird recognition using Haar cascades.
- [x] Development of a real-time bird detection program using a trained model and the capabilities of the open-cv library.
- [x] Research and documentation:
    - [x] Documentation.
    - [x] GitHub Page.
    - [x] Presentation.
    - [x] Copyright certificate.
    - [x] Other important documents.
- [ ] Train the algorithm to 92%+ accuracy of bird recognition based on thousands of positive and negative data.
- [ ] Optimize the bird recognition program to reduce delays and improve real-time performance.
- [ ] Development of a test model of an automated bird-repelling device based on Raspberry PI.
- [ ] Improving technology, expanding capabilities, increasing accuracy, speed and reliability:
    - [ ] Solving the problem of birds colliding with power lines.
    - [ ] Solving the problem of birds colliding with wind farms.

## Getting Started

### Dependencies

Install OpenCV-Python library:
   ```
   pip install opencv-python
   ```

### Installing

Clone the repo:
   ```sh
   git clone https://github.com/silvermete0r/OmenFlightAI.git
   ```

### Executing program

Just execute the `BirdsDetectionByHaarCascades.py` file.

## Help

Contributions are what makes the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "birds".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/something...`)
3. Commit your Changes (`git commit -m 'Add some something...'`)
4. Push to the Branch (`git push origin feature/something...`)
5. Open a Pull Request

## Authors

* Arman Zhalgasbayev - 
[@grembim](https://www.instagram.com/grembim)

* Aldabegenov Makhambet - 
[@elliotdewitt169](https://www.instagram.com/elliotdewitt169)

* Aidarova Anel - 
[@dlighti](https://www.instagram.com/dlighti)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details

## Acknowledgments

* [Awesome-ReadMe](https://github.com/matiassingers/awesome-readme)
* [Birds-Detection-OpenCV](https://github.com/yenusu/OpenCV-Birds-Detection-Algorithm)
* [HaarCascades-For-Birds-Detection](https://github.com/Souravjyoti/Bird_detection)
* [Haar-Cascades](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html)
* [Haar-Cascades-Training](https://github.com/mrnugget/opencv-haar-classifier-training)




<!-- MARKDOWN LINKS & IMAGES -->
[birds-test]: https://sun9-west.userapi.com/sun9-5/s/v1/ig2/_F_u3FaRel-aT3OEO25hPe2BxMDfJn-qlUfwvDemc17tVL4TkW8JpvSSEKkQ_Fgl7yjnBIY9ofedUPffSbHQ9AfK.jpg?size=2224x1098&quality=95&type=album
[link]: https://miro.medium.com/max/1100/1*iLS7tWM9hfWNZGeBnv3qgA.png
