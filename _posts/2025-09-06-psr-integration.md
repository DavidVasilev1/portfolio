---
title: Purdue Solar Racing - Integration
author: david
categories: ['Manufacturing', 'Design']
tags: ['CAD', 'FEA', '3D Printing', 'NX', 'Simcenter', 'Altair Hypermesh', 'Integration', 'Leadership', 'Teamcenter', 'PDM', 'Top-Down Modeling']
description: Led Purdue Solar Racing as Chief Engineer, developing a carbon fiber monocoque chassis and integrating complex mechanical and electrical systems for the 2026 solar car competition.
toc: True
comments: True
date: 2025-09-06 12:00:00 +0000
published: true
image: /assets/img/post_images/psr/solar_thumbnail2.png
---

<style>
  .responsive-slideshow {
    position: relative;
    padding-bottom: 56.25%; /* 16:9 aspect ratio */
    height: 0;
    overflow: hidden;
    max-width: 100%;
  }

  .responsive-slideshow iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border: 0;
  }
</style>

![Team](/assets/img/post_images/psr/solar_thumbnail2.png)
*Integration*{: style="font-size:1.2em; display:block; text-align:center;"}


## PDM Design

### Version 1
I began by designing a custom ID system for Teamcenter, but quickly deprecated this approach after encountering limitations with Purdue’s system configuration.

![PDM](/assets/img/post_images/psr/integration/pdm3.png){: width="700"}
*Designed a custom ID system for Teamcenter — later deprecated due to system limitations.*{: style="font-size:1.2em; display:block; text-align:center;"}

![PDM](/assets/img/post_images/psr/integration/pdm4.png){: width="700"}
*Developed a checkout process to ensure no overwriting of critical parts.*{: style="font-size:1.2em; display:block; text-align:center;"}

### Version 2
I pivoted to Box Drive, aligning with other car teams and gaining greater flexibility for part IDs, file control, and version management. While not perfect, this system proved robust for our needs.

![PDM](/assets/img/post_images/psr/integration/pdm1.png){: width="700"}
*Implemented a Box Drive ID system to improve flexibility and file control.*{: style="font-size:1.2em; display:block; text-align:center;"}

![PDM](/assets/img/post_images/psr/integration/pdm5.png){: width="700"}
*Established a part checkout/locking process to prevent merge conflicts.*{: style="font-size:1.2em; display:block; text-align:center;"}

## WAVE Linking
Faced with scarce resources on WAVE linking and top-down modeling, I proactively researched methodologies by consulting with interns from SpaceX, Zipline, and Relativity. This effort directly shaped the development of our current WAVE linking workflow.

![WAVE Linking](/assets/img/post_images/psr/integration/wavelinking6.png){: width="700"}
*Created a reference assembly for WAVE linking, ensuring static objects preserve link integrity.*{: style="font-size:1.2em; display:block; text-align:center;"}

![WAVE Linking](/assets/img/post_images/psr/integration/wavelinking7.png){: width="700"}
*Documented a comprehensive WAVE linking process for consistent integration.*{: style="font-size:1.2em; display:block; text-align:center;"}

![WAVE Linking](/assets/img/post_images/psr/integration/wavelinking8.png){: width="700"}
*Produced a simple model demonstrating pin creation using a WAVE linked face.*{: style="font-size:1.2em; display:block; text-align:center;"}

![WAVE Linking](/assets/img/post_images/psr/integration/wavelinking1.png){: width="700"}
*Delivered a finalized assembly demonstrating the WAVE linking process in action.*{: style="font-size:1.2em; display:block; text-align:center;"}

![WAVE Linking](/assets/img/post_images/psr/integration/wavelinking2.png){: width="700"}
*Managed link integrity through the Interpart Link Browser, quickly identifying broken and updated references.*{: style="font-size:1.2em; display:block; text-align:center;"}

### Issues Encountered

![WAVE Linking](/assets/img/post_images/psr/integration/wavelinking3.png){: width="700"}
*Discovered that some links failed to update due to load settings — prompting a redesign of our workflow.*{: style="font-size:1.2em; display:block; text-align:center;"}

![WAVE Linking](/assets/img/post_images/psr/integration/wavelinking5.png){: width="700"}
*Encountered broken WAVE links requiring manual fixes, highlighting the need for a more robust system.*{: style="font-size:1.2em; display:block; text-align:center;"}

### Solutions
After iterative development and extensive research, I established the current PDM methodology — a system still evolving as we encounter new challenges.

<div class="responsive-slideshow">
  <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQWid3Nvl50vPgn4XXB72MvQCD4tB_mRSz28VoR0A9bnPoBNIuoC64oZmJChkEVf7U-YdZHihmR4vAT/embed?start=false&loop=false&delayms=3000" 
          frameborder="0" 
          allowfullscreen="true" 
          mozallowfullscreen="true" 
          webkitallowfullscreen="true"></iframe>
</div>

Looking ahead, I plan to entirely rework this system, adopting a “sandbox” assembly approach. Each part will be created independently, with no direct links to the master assembly. This will give users maximum freedom to modify parts without disrupting the core structure. Final assemblies will integrate completed parts cleanly, ensuring stability while allowing creative flexibility.

## Integration

![Integration](/assets/img/post_images/psr/integration/integration3.png){: width="700"}
*I calculate the preliminary CG using bounding boxes with assigned masses. This method gives a quick estimate of dynamics to guide suspension design for stability.*{: style="font-size:1.2em; display:block; text-align:center;"}

![Integration](/assets/img/post_images/psr/integration/integration5.png){: width="700"}
*I define selective coring to integrate the roll cage and suspension.*{: style="font-size:1.2em; display:block; text-align:center;"}

### Structures

![Structures](/assets/img/post_images/psr/integration/structures4.png){: width="700"}
*I integrate structures by combining the chassis, cross-chassis supports, battery box and supports, and occupant cell. Selective coring strengthens the chassis where mounts attach.*{: style="font-size:1.2em; display:block; text-align:center;"}

![Structures](/assets/img/post_images/psr/integration/structures2.png){: width="700"}
*I integrate the aeroshell with the cross-chassis supports and mechanical systems. We position the cross-chassis supports to optimize load transfer into the chassis and aeroshell.*{: style="font-size:1.2em; display:block; text-align:center;"}

![Structures](/assets/img/post_images/psr/integration/structures3.png){: width="700"}
*I define mounting points for the top shell hinging, supports, and latches. Red marks hinges, green marks telescoping supports, and blue marks latches.*{: style="font-size:1.2em; display:block; text-align:center;"}

![Structures](/assets/img/post_images/psr/integration/structures5.png){: width="700"}
*I designed the battery support structure and housing at the rear of the chassis. The angled supports guide the battery into position, secure it with ratcheted restraints, and allow quick removal and placement.*{: style="font-size:1.2em; display:block; text-align:center;"}

### Brakes
![Brakes](/assets/img/post_images/psr/integration/brakes3.png){: width="700"}
*We originally mounted the master cylinders to the front of the chassis. After cutting the chassis front for accessibility, we relocated them to the top using a bracket.*{: style="font-size:1.2em; display:block; text-align:center;"}

![Brakes](/assets/img/post_images/psr/integration/brakes2.png){: width="700"}
*We moved the master cylinders to the chassis side chamfer to gain clearance while keeping them above the brake lines.*{: style="font-size:1.2em; display:block; text-align:center;"}

![Brakes](/assets/img/post_images/psr/integration/brakes4.png){: width="700"}
*After modifying the chassis front, we top-mounted the master cylinders with a bracket. We also positioned the hand brake between the front suspension and roll cage, within driver reach.*{: style="font-size:1.2em; display:block; text-align:center;"}

### Dynamics
![Dynamics](/assets/img/post_images/psr/integration/steering1.png){: width="700"}
*We integrate steering with the chassis by using a gearbox to transfer motion into the steering rack, which runs through the chassis walls to the uprights.*{: style="font-size:1.2em; display:block; text-align:center;"}

![Dynamics](/assets/img/post_images/psr/integration/steering2.png){: width="700"}
*We identified an issue with placing a chassis hole too close to the suspension hardpoints. We used the L/D ratio to check the distance from the hole edge to the mounting point.*{: style="font-size:1.2em; display:block; text-align:center;"}

![Dynamics](/assets/img/post_images/psr/integration/steering3.png){: width="700"}
*The analysis showed the hole was too close, with an L/D ratio of 1.71 and a safety factor of 2. We responded by moving the steering rack farther from the hardpoints.*{: style="font-size:1.2em; display:block; text-align:center;"}

![Dynamics](/assets/img/post_images/psr/integration/steering4.png){: width="700"}
*We repositioned the steering farther from the suspension hardpoints for safety and structural integrity.*{: style="font-size:1.2em; display:block; text-align:center;"}

![Dynamics](/assets/img/post_images/psr/integration/suspension1.png){: width="700"}
*We set initial suspension hardpoints using a simple rocker and shock model to determine component placement.*{: style="font-size:1.2em; display:block; text-align:center;"}

![Dynamics](/assets/img/post_images/psr/integration/suspension2.png){: width="700"}
*We aligned the pushrod angle with the chassis surface to integrate suspension with the chassis. The dynamics team calculated optimal positioning to maximize stability.*{: style="font-size:1.2em; display:block; text-align:center;"}

### Roll Cage

### Electrical
![Electrical](/assets/img/post_images/psr/integration/battery1.png){: width="700"}
*Selective coring defined for integration with roll cage and suspension.*{: style="font-size:1.2em; display:block; text-align:center;"}

![Electrical](/assets/img/post_images/psr/integration/battery2.png){: width="700"}
*Selective coring defined for integration with roll cage and suspension.*{: style="font-size:1.2em; display:block; text-align:center;"}

![Electrical](/assets/img/post_images/psr/integration/battery3.png){: width="700"}
*Selective coring defined for integration with roll cage and suspension.*{: style="font-size:1.2em; display:block; text-align:center;"}

![Electrical](/assets/img/post_images/psr/integration/electrical1.png){: width="700"}
*Selective coring defined for integration with roll cage and suspension.*{: style="font-size:1.2em; display:block; text-align:center;"}

![Electrical](/assets/img/post_images/psr/integration/electrical2.png){: width="700"}
*Selective coring defined for integration with roll cage and suspension.*{: style="font-size:1.2em; display:block; text-align:center;"}
