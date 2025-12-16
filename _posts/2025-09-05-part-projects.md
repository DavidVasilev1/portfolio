---
title: Purdue Aerial Robotics Team
author: david
categories: ['Manufacturing', 'Design']
tags: ['CAD', 'FEA', '3D Printing', 'NX', 'Simcenter']
description: Member of Purdue Aerial Robotics Team, handling avionics and optics. Performed FEA, thermal and electrical analysis, and designed wiring layouts to optimize system performance for the 2025 competition.
toc: True
comments: True
date: 2025-09-05 12:00:00 +0000
published: true
image: /assets/img/post_images/part/part_thumbnail.png
---
## Avionics Layout

![layout1](/assets/img/post_images/part/layout1.png){: width="700"}
![layout2](/assets/img/post_images/part/layout2.png){: width="700"}

## Mounts

These mounts were designed to hold various avionics components in place in flight and during crash scenarios without failing.

### Initial Design

The initial mounts I designed to hold the Nvidia Jetson (left) and the communications and control module (right) with the following mounts. I designed the control module to dampen vibrations because the control module mounted on top holds an IMU, which is typically sensitive to vibrations.

![mounts1](/assets/img/post_images/part/mounts1.png){: width="700"}
![mounts2](/assets/img/post_images/part/mounts2.png){: width="700"}

Finite Element Analysis (FEA) was performed in Simcenter. I used isotropic properties and approximated the 3D printer infill by setting the PLA density to a corresponding percentage of its actual density.

![mountfea1](/assets/img/post_images/part/mountfea1.png){: width="700"}
![mountfea2](/assets/img/post_images/part/mountfea2.png){: width="700"}

This mounting method was discontinued because it was a couple of millimeters too tall to fit in the fuselage, which needed to be as small as possible due to competition sizing constraints.

### Final Design

This is the final design which was placed in the aircraft for flight testing. Despite the plane crashing multiple times, the mounts I designed never failed due to the FEA and optimization I conducted.

This first component is the modified electronic stack mount. Its height was reduced to improve clearance and ensure an optimal fit within the restricted fuselage space. Due to the tight spatial constraints, vibration dampening mechanisms could not be integrated into this specific design iteration.
![mountfea4](/assets/img/post_images/part/mountfea4.png){: width="700"}
*FEA shows minimal displacement in the event of a crash.*{: style="font-size:1.2em; display:block; text-align:center;"}
![mounts3](/assets/img/post_images/part/mounts3.JPG){: width="700"}

The Jetson mounting solution was engineered to maximize space efficiency. It positions the Jetson unit at the lowest feasible point within the fuselage to ensure full compliance with the airframe's internal geometry and volumetric limits.
![mountfea3](/assets/img/post_images/part/mountfea3.png){: width="700"}
*FEA shows minimal displacement in the event of a crash.*{: style="font-size:1.2em; display:block; text-align:center;"}
![mounts4](/assets/img/post_images/part/mounts4.JPG){: width="700"}

The camera mounting mechanism utilizes a quick-release clip design, inspired by the functionality of a standard GoPro mount. FEA simulations validated the design, specifically showing the necessary elastic deformation (displacement) when squeezed, which allows the clip to successfully attach to the mating bracket.
![mountfea5](/assets/img/post_images/part/mountfea5.png){: width="700"}

These custom-designed battery holders serve a critical function during manufacturing: securing the individual cells in their precise final arrangement. This fixed configuration allowed for efficient soldering of the cells into the desired pack shape before being heat shrink-wrapped for electrical isolation from the conductive carbon fiber fuselage.
![batterymounts1](/assets/img/post_images/part/batterymounts1.JPG){: width="700"}
![batterymounts2](/assets/img/post_images/part/batterymounts2.JPG){: width="700"}
![batterymounts3](/assets/img/post_images/part/batterymounts3.JPG){: width="700"}

## Integration

The following images show my mounts integrated onto the airplane.

![integration1](/assets/img/post_images/part/integration1.png){: width="700"}
![integration2](/assets/img/post_images/part/integration2.png){: width="700"}

## Final Product

![plane2](/assets/img/post_images/part/plane2.png){: width="700"}