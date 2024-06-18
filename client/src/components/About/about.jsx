import React from "react";
import './about.css';
import Abt from "../Cards/Abt-crd/abt-crd";

function About(){
    return(
        <div className="abtcards">
            <div className="abttitle">
                <h2>About Us</h2>
            </div>
            <div className="titldes"> 

           
            <Abt 
                title="Title"
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam euismod, nisi vel consectetur euismod, nisl nisl aliquam nisl, eu aliquam nisl nisl eu nisl. Nulla facilisi. Aenean commodo consequat urna, nec gravida felis facilisis id. Duis nec lorem non metus consectetur accumsan. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tincidunt quam a elit ornare, a pellentesque libero vehicula. Donec vel laoreet urna, a viverra augue. Suspendisse potenti."
            />
             <Abt 
                title="Title"
                description="Vestibulum eget arcu nec neque consequat fringilla. Quisque non mauris eu nulla luctus congue. Etiam varius massa sit amet urna suscipit facilisis. Integer feugiat, justo at hendrerit tempor, justo sapien sagittis quam, eu sodales risus turpis et lectus. In hac habitasse platea dictumst. Curabitur blandit fringilla est non dapibus. Curabitur vitae posuere sem. Vivamus fermentum ipsum eget odio varius, ac fringilla libero condimentum. Etiam eu felis nec ligula feugiat sodales. Fusce sed velit ut dolor tincidunt ultrices. Proin ut quam lacus. Suspendisse potenti."
            />
             <Abt 
                title="Title"
                description="Mauris sodales, sapien eu suscipit malesuada, lacus est tristique metus, a sollicitudin lorem lectus eu urna. Vestibulum et urna libero. Nam sit amet ipsum at odio venenatis laoreet. Donec viverra, libero at feugiat finibus, urna nulla elementum magna, nec varius odio mi nec ligula. Cras dapibus leo id urna convallis, at fermentum massa sagittis. Proin vestibulum, mi in tincidunt sodales, lorem leo facilisis nisi, id scelerisque metus magna et sapien. Nullam vulputate justo id libero laoreet, nec vehicula nisi tincidunt. Fusce et erat a urna volutpat tincidunt id nec elit. Nullam hendrerit ante eros, nec sagittis felis luctus ut."
            />
             </div>
            
        </div>
    )
}

export default About;