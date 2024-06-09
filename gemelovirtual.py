<!DOCTYPE html>
<html>
	<head lang="en">
		<meta charset="utf-8">
		<title>My first three.js app</title>
		<style>
			body { margin: 0; }
		</style>
		<script src="https://cdn.jsdelivr.net/npm/three@0.126.1/build/three.min.js"></script>
	</head>
	<body>
        <div id="arm"></div>
        <h2>Servo_1</h2>
        <input type="text" id="Texto_servo1" placeholder="Ingrese el grado deseado">
        <h2>Servo_2</h2>
        <input type="text" id="Texto_servo2" placeholder="Ingrese el grado deseado">
        <h2>Motor_1</h2>
        <input type="text" id="MiCampoDeTexto2" placeholder="Ingrese 0 o 1">
        <h2>Motor_2</h2>
        <input type="text" id="MiCampoDeTexto3" placeholder="Ingrese 0 o 1">
        
        <button onclick="mover_servo1()"> MOVER SERVO1 </button>
        <button onclick="mover_servo2()"> MOVER SERVO2 </button>
        <button onclick="mover_motores()"> MOVER MOTORES </button>
        <button onclick="baile()"> BAILE </button>
		<div id="error"></div>
		
		<meta charset="UTF-8">
		
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tabla</title>
        <style>
            table {
                border-collapse: collapse;
                width: 100%;
            }
            th, td {
                border: 1px solid #dddddd;
                text-align: left;
                padding: 8px;
            }
            th {
                background-color: #f2f2f2;
            }
            .indent {
                padding-left: 20px; /* Ajusta el nivel de indentación */
            }
    
        </style>
        </head>
        <body>

        <table>
          <tr>
            <th>Pieza</th>
            <th>Medida ancho</th>
            <th>Medida alto</th>
            <th>Medida largo</th>
            <th>Medida radio</th>
          </tr>
          <tr>
            <td>Llanta1</td>
            <td>2,5</td>
            <td>x</td>
            <td>x</td>
            <td>6</td>
          </tr>
          <tr>
            <td>Llanta2</td>
            <td>2,5</td>
            <td>x</td>
            <td>x</td>
            <td>6</td>
          </tr>
          <tr>
            <td>Llanta3</td>
            <td>1,3</td>
            <td>x</td>
            <td>x</td>
            <td>2,5</td>
          </tr>
          <tr>
            <td>servo1</td>
            <td>3</td>
            <td>3</td>
            <td>1</td>
            <td>x</td>
          </tr>
          <tr>
            <td>servo2</td>
            <td>3</td>
            <td>3</td>
            <td>1</td>
            <td>x</td>
          </tr>
          <tr>
            <td>base</td>
            <td>9.5</td>
            <td>0.3</td>
            <td>14.5</td>
            <td>x</td>
          </tr>
          <tr>
            <td>proto</td>
            <td>6.5</td>
            <td>1</td>
            <td>17</td>
            <td>x</td>
          </tr>
          <tr>
            <td>raswery</td>
            <td>2.1</td>
            <td>0.2</td>
            <td>5.2</td>
            <td>x</td>
          </tr>
          <tr>
            <td>rojo</td>
            <td>4</td>
            <td>0.2</td>
            <td>4</td>
            <td>x</td>
          </tr>
          <tr>
            <td>soporte1</td>
            <td>5</td>
            <td>0.3</td>
            <td>5</td>
            <td>x</td>
          </tr>
          <tr>
            <td>soporte2</td>
            <td>5</td>
            <td>0.3</td>
            <td>5</td>
            <td>x</td>
          </tr>
          <tr>
            <td>paloservo1</td>
            <td>0.7</td>
            <td>0.3</td>
            <td>4</td>
            <td>x</td>
          </tr>
          <tr>
            <td>paloservo2</td>
            <td>1.2</td>
            <td>0.3</td>
            <td>9</td>
            <td>x</td>
          </tr>
          <tr>
            <td>paloservo2_union_paloservo1</td>
            <td>1.2</td>
            <td>0.3</td>
            <td>9</td>
            <td>x</td>
          </tr>
          <tr>
            <td>union</td>
            <td>2.4</td>
            <td>0.3</td>
            <td>6</td>
            <td>x</td>
          </tr>
          <tr>
            <td>paloservo2</td>
            <td>1.2</td>
            <td>0.3</td>
            <td>9</td>
            <td>x</td>
          </tr>
          <tr>
            <td>piedearbol</td>
            <td>3.5</td>
            <td>0.3</td>
            <td>4.5</td>
            <td>x</td>
          </tr>
          <tr>
            <td>articulacion1</td>
            <td>0.6</td>
            <td>0.3</td>
            <td>8.7</td>
            <td>x</td>
          </tr>
          <tr>
            <td>motor1</td>
            <td>2.2</td>
            <td>2.2</td>
            <td>6.4</td>
            <td>x</td>
          </tr>
          <tr>
            <td>motor2</td>
            <td>2.2</td>
            <td>2.2</td>
            <td>6.4</td>
            <td>x</td>
          </tr>
        </table>
		
		<script  >
        document.write((new Date()).toLocaleTimeString(),'b');
        
        // Definición de las medidas para cada pieza como arrays [ancho, alto, largo, radio]
        let llanta1 = [2.5, null, null, 6];
        let llanta2 = [2.5, null, null, 6];
        let llanta3 = [1.3, null, null, 2.5];

        let servo11 = [3, 3, 1, null];
        let servo22 = [3, 3, 1, null];

        let base11 = [9.5, 0.3, 14.5, null];
        let proto11 = [6.5, 1, 14, null];
        let raswery11 = [2.1, 0.2, 5.2, null];
        let rojo11 = [4, 0.2, 4, null];
        let soporte11 = [5, 0.3, 5, null];
        let soporte22 = [5, 0.3, 5, null];
        let paloservo11 = [0.7, 0.3, 4, null];
        let paloservo22 = [1.2, 0.3, 9, null];
        let paloservo2_union_paloservo1 = [1.2, 0.3, 9, null];
        let union11 = [2.4, 0.3, 6, null];
        let piedearbol11 = [3.5, 0.3, 4.5, null];
        let articulacion11 = [0.6, 0.3, 8.7, null];
        let motor11 = [2.2, 2.2, 6.4, null];
        let motor22 = [2.2, 2.2, 6.4, null];

		// Set up Three.js scene and camera
		const width = window.innerWidth;
		const height = window.innerHeight / 2;
		const scene = new THREE.Scene();
		const camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 1000);

        camera.position.x = 0;
		camera.position.y = 5;
		camera.position.z = 0;
		camera.lookAt(0, 0, 0);

		// Define a point in 3D space
		const point = new THREE.Vector3();

		// Set initial LED color and arm dimensions
		let color_led =  0x00fff0;
		let color_led1 = 0x0000ff;
		let color_led2 = 0x00ff00;
		let color_led3 = 0xffffff;
		let color_led4 = 0xA0522D;
	    let color_led5 = 0xDAA520;
	    let color_led6 = 0xFFFF00;
	    let color_led7 = 0xFF0000;
				
        const a1 = 1;
		const a2 = 2;
		const a3 = 2;

		// Create WebGL renderer and append it to the DOM
		const renderer = new THREE.WebGLRenderer();
		renderer.setSize(width, height);
		const arm_DOM = document.getElementById("arm");
		arm_DOM.appendChild(renderer.domElement);

		// Define a small dot for visualization
		let dot = new THREE.BoxGeometry(0.01, 0.01, 0.01);

		// error label
		const error_DOM = document.getElementById("error");
		error_DOM.innerHTML = "Error="

		// Set up the base of the mechanical arm
		let material1 = new THREE.MeshBasicMaterial({ color: color_led1 }); //azul
		let material2 = new THREE.MeshBasicMaterial({ color: color_led2 }); //verde
		let material3 = new THREE.MeshBasicMaterial({ color: color_led3 }); //blanco
		let material4 = new THREE.MeshBasicMaterial({ color: color_led4 }); //cafe
		let material5 = new THREE.MeshBasicMaterial({ color: color_led5 }); //cafe claro
		let material6 = new THREE.MeshBasicMaterial({ color: color_led6 }); //amarillo
		let material7 = new THREE.MeshBasicMaterial({ color: color_led7 }); //rojo
		
		// ancho, alto, largo
		
		let baseA = base11[2]/3;
	    let baseB = base11[1]/3;
		let baseC = base11[0]/3;
		
		let protoA = proto11[2]/3;
		let protoB = proto11[1]/3;
		let protoC = proto11[0]/3;
		
		let servitisA = servo11[2]/3;
		let servitisB = servo11[1]/3;
		let servitisC = servo11[0]/3;
		
		let rasweryA = raswery11[2]/3;
		let rasweryB = raswery11[1]/3;
		let rasweryC = raswery11[0]/3;
		
		let controlA = rojo11[2]/3;
		let controlB = rojo11[1]/3;
		let controlC = rojo11[0]/3;
		
		let soporte11A = soporte11[2]/3;
		let soporte11B = soporte11[1]/3;
		let soporte11C = soporte11[0]/3;
		
	    let geometry = new THREE.BoxGeometry( baseA, baseB, baseC);
	    let geometry3 = new THREE.BoxGeometry(protoA, protoB , protoC);
		let geometry4 = new THREE.BoxGeometry(servitisA, servitisB , servitisC );
		let geometry5 = new THREE.BoxGeometry(rasweryA, rasweryB , rasweryC );
		let geometry6 = new THREE.BoxGeometry(controlA, controlB, controlC);
		let geometry7 = new THREE.BoxGeometry(soporte11A, soporte11B, soporte11C);
		 //Z (+) DERECHA , Y (+) ARRIBA, X (+) ATRAS 
		
		const base = new THREE.Mesh(geometry, material5);
		base.translateY(a1 / 2);
		scene.add(base);
		
		let geometry8 = new THREE.BoxGeometry( 1.4, 0.1, 0.8);
		const piedearbol = new THREE.Mesh(geometry8, material5);
		piedearbol.rotation.x = Math.PI / 2;
		piedearbol.rotation.z = Math.PI / 2;
		piedearbol.translateZ(-0.5);
		base.add(piedearbol);
		
		const piedearbol2 = new THREE.Mesh(geometry8, material5);
		piedearbol2.rotation.x = Math.PI / 2;
		piedearbol2.rotation.z = Math.PI / 2;
		piedearbol2.translateZ(-0.5);
		piedearbol2.translateY(1.8);
		base.add(piedearbol2);
		
		const soporte1 = new THREE.Mesh(geometry7, material5);
		soporte1.rotation.x = Math.PI / 2;
		soporte1.translateY(0.8);
		soporte1.translateZ(-0.8);
		soporte1.translateX(-1);
		base.add(soporte1);
		
		const soporte2 = new THREE.Mesh(geometry7, material5);
		soporte2.rotation.x = Math.PI / 2;
		soporte2.translateY(-0.8);
		soporte2.translateZ(-0.8);
		soporte2.translateX(-1);
		base.add(soporte2);
		
		const proto = new THREE.Mesh(geometry3, material3);
		proto.translateY(0.2);
	    proto.translateX(2.8);
		base.add(proto);
		
		const servitis1 = new THREE.Mesh(geometry4, material1);
		servitis1.rotation.z = Math.PI / 2;
		servitis1.translateY(1);
	    servitis1.translateX(0.5);
	    servitis1.translateZ(1);
		base.add(servitis1);
		
		const servitis2 = new THREE.Mesh(geometry4, material1);
		servitis2.rotation.z = Math.PI / 2;
		servitis2.translateY(1);
	    servitis2.translateX(0.5);
	    servitis2.translateZ(-1);
		base.add(servitis2);
		
		const raswery = new THREE.Mesh(geometry5, material2);
		raswery.translateY(a1 / 2);
	    raswery.translateX(4);
		base.add(raswery);
		
		const control = new THREE.Mesh(geometry6, material7);
		control.translateY(a1 / 2);
	    control.translateX(3);
		base.add(control);
		
		let llanta1A = llanta1[0]/3;
		let llanta1B = llanta1[3]/3;
		
		let llanta3A = llanta3[0]/3;
		let llanta3B = llanta3[3]/3;
		
		const wheelGeometry = new THREE.CylinderGeometry(llanta1A, 1, 0.2, 32); // Radio superior, radio inferior, altura, segmentos
        const wheelGeometry1 = new THREE.CylinderGeometry(llanta3A, 0.5, 0.2, 32);
        const wheelGeometry2 = new THREE.CylinderGeometry(llanta3A/2 , 0.6, 0.2, 32);
        
        // Crear materiales para las ruedas
        const wheelMaterial = new THREE.MeshBasicMaterial({ color: 0x555555 });

        // Crear objetos de las ruedas
        const wheel1 = new THREE.Mesh(wheelGeometry, wheelMaterial);
        const wheel2 = new THREE.Mesh(wheelGeometry, wheelMaterial);
        const wheel3 = new THREE.Mesh(wheelGeometry1, wheelMaterial);
        const wheel33 = new THREE.Mesh(wheelGeometry2, material3);
        const wheel4 = new THREE.Mesh(wheelGeometry1, material6);
        const wheel5 = new THREE.Mesh(wheelGeometry1, material6);


        // Posicionar las ruedas
        wheel1.position.set(1, -1 , 1.2); // Ajusta las coordenadas según tu escena
        wheel2.position.set(1, -1, -1.2); // Ajusta las coordenadas según tu escena
        wheel3.position.set(-1, -1, -0.1); // Ajusta las coordenadas según tu escena
        wheel33.position.set(-1, -1, -0.1); // Ajusta las coordenadas según tu escena
        wheel4.position.set(1, -1, 1.2); // Ajusta las coordenadas según tu escena
        wheel5.position.set(1, -1, -1.2); // Ajusta las coordenadas según tu escena

        // Conectar las ruedas a la base
        base.add(wheel1);
        base.add(wheel2);
        base.add(wheel3);
        base.add(wheel33);
        base.add(wheel4);
        base.add(wheel5);
        
        //Ponerlos verticalmente
        wheel1.rotation.x = Math.PI / 2;
        wheel2.rotation.x = Math.PI / 2;
        wheel3.rotation.x = Math.PI / 2;
        wheel33.rotation.x = Math.PI / 2;
        wheel4.rotation.x = Math.PI / 2;
        wheel5.rotation.x = Math.PI / 2;
            
        // Create hierarchical structure for the arm segments
		let shoulder = new THREE.Object3D();
		shoulder.translateY(a1 / 2);
		base.add(shoulder);

		geometry = new THREE.BoxGeometry(0.05, a2, 0.3);
		let lowerArm = new THREE.Mesh(geometry, material4);
		lowerArm.translateY(a2 / 2);
		shoulder.add(lowerArm);

		let elbow = new THREE.Object3D();
		elbow.translateY(a2 / 2);
		lowerArm.add(elbow);
		
		let arm = new THREE.Mesh(geometry, material4);
		arm.translateY(a3 / 2);
		elbow.add(arm);
		            
        let wrist = new THREE.Object3D();
		wrist.translateY(a3 / 2);
		arm.add(wrist);
		
		
		// Set up parameters for a line to visualize the arm trajectory
		const MAX_POINTS = 1000;
		material = new THREE.LineBasicMaterial({ color: 0xff00ff });
		geometry = new THREE.BufferGeometry();
		const positions = new Float32Array(MAX_POINTS * 3);
		let last_point = 0;

		// Set initial positions for the arm trajectory line
		geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
		const line = new THREE.Line(geometry, material);
		scene.add(line);

        // Define two points for the Bezier curve
		const P0 = new THREE.Vector3(a2, a1 / 2, -a3);
		const P1 = new THREE.Vector3(a2, a1 / 2, a3);
		var t = 0;

		var P0_camara = new THREE.Vector3(6, 2, 5);
		var P1_camara = new THREE.Vector3(0, 0, 5);
		var t_camara=0
		
        // Start the animation loop3
        animate();
        
		function animate() {
		    //if (t <= 1) {
			//	requestAnimationFrame(animate);
			//}
			
			// Calculate inverse kinematics and update arm positions
			let th1p, th2p, th3p, R;
			R = bezier2(P0, P1, t);
			[th1p, th2p, th3p] = inv_kin(R);
			// Loop through the Bezier curve parameter
			if (t <= 1) {
				t = t + 0.01;
			}


			base.rotation.y = th1p;
			shoulder.rotation.z = Math.PI / 2 + th2p;
			elbow.rotation.z = th3p;

			// Visualize the position of the wrist with a dot
			let dot_i = new THREE.Mesh(dot, material2);
			wrist.getWorldPosition(point);
			scene.add(dot_i);
            
            // Update the arm trajectory line
			positions[last_point] = point.x;
			positions[last_point + 1] = point.y;
			positions[last_point + 2] = point.z;
			last_point = last_point + 3;
			line.geometry.attributes.position.needsUpdate = true;
			error_DOM.innerHTML = "Error="+R.distanceTo(point)
			
			R_camara = bezier2(P0_camara, P1_camara, t_camara);
			camera.position.set(R_camara.x,R_camara.y,R_camara.z)
			//console.log(camera.position)
			camera.lookAt(0, 0, 0)
			if (t_camara <= 1) {
				t_camara = t_camara + 0.00033;
			}
			else {
				t_camara = 0
			}

			// Render the scene
			renderer.render(scene, camera);
}

            function mover_servo1() {
                // Obtener el valor del ángulo deseado del servo1 (lower arm) del campo de texto
                const nuevoAnguloTexto = document.getElementById("Texto_servo1").value;

                // Convertir el valor del ángulo deseado del servo1 de grados a radianes usando THREE.Math.degToRad()
                const nuevoAngulo = THREE.Math.degToRad(parseFloat(nuevoAnguloTexto));

                // Obtener la rotación actual del hombro del servo1 (lower arm)
                const rotacionActualShoulder = shoulder.rotation.y;

                // Calcular la rotación adicional en el eje Y para mantener la orientación frontal inicial
                const diferenciaAnguloShoulder = -rotacionActualShoulder;

                // Aplicar la rotación adicional en el eje Y al objeto shoulder
                shoulder.rotation.y += diferenciaAnguloShoulder;

                // Obtener la rotación actual del codo del servo1 (lower arm)
                const rotacionActualLowerArm = lowerArm.rotation.z;

                // Calcular la diferencia de ángulo entre el ángulo actual y el nuevo ángulo para el servo1 (lower arm)
                const diferenciaAnguloLowerArm = nuevoAngulo - rotacionActualLowerArm;

                // Aplicar la rotación al servo1 (lower arm)
                lowerArm.rotation.z = nuevoAngulo;

                // Ajustar la posición del servo1 (lower arm) para que no se despegue del shoulder
                lowerArm.position.y = a1 / 2;
                lowerArm.position.z = -a1 * Math.cos(nuevoAngulo) + a2 / 2 * Math.cos(lowerArm.rotation.z);
                lowerArm.position.x = a1 * Math.sin(nuevoAngulo) - a2 / 2 * Math.sin(lowerArm.rotation.z);

                // Renderizar la escena para actualizar los cambios
                renderer.render(scene, camera);
            }

            function mover_servo11( nuevoAnguloTexto ) {

                // Convertir el valor del ángulo deseado del servo1 de grados a radianes usando THREE.Math.degToRad()
                const nuevoAngulo = THREE.Math.degToRad(parseFloat(nuevoAnguloTexto));

                // Obtener la rotación actual del hombro del servo1 (lower arm)
                const rotacionActualShoulder = shoulder.rotation.y;

                // Calcular la rotación adicional en el eje Y para mantener la orientación frontal inicial
                const diferenciaAnguloShoulder = -rotacionActualShoulder;

                // Aplicar la rotación adicional en el eje Y al objeto shoulder
                shoulder.rotation.y += diferenciaAnguloShoulder;

                // Obtener la rotación actual del codo del servo1 (lower arm)
                const rotacionActualLowerArm = lowerArm.rotation.z;

                // Calcular la diferencia de ángulo entre el ángulo actual y el nuevo ángulo para el servo1 (lower arm)
                const diferenciaAnguloLowerArm = nuevoAngulo - rotacionActualLowerArm;

                // Aplicar la rotación al servo1 (lower arm)
                lowerArm.rotation.z = nuevoAngulo;

                // Ajustar la posición del servo1 (lower arm) para que no se despegue del shoulder
                lowerArm.position.y = a1 / 2;
                lowerArm.position.z = -a1 * Math.cos(nuevoAngulo) + a2 / 2 * Math.cos(lowerArm.rotation.z);
                lowerArm.position.x = a1 * Math.sin(nuevoAngulo) - a2 / 2 * Math.sin(lowerArm.rotation.z);

                // Renderizar la escena para actualizar los cambios
                renderer.render(scene, camera);
            }



            function mover_servo2() {
                // Obtener el valor del ángulo deseado del servo2 (arm) del campo de texto
                const nuevoAnguloTexto = document.getElementById("Texto_servo2").value;

                // Convertir el valor del ángulo deseado del servo2 de grados a radianes usando THREE.Math.degToRad()
                const nuevoAngulo = THREE.Math.degToRad(parseFloat(nuevoAnguloTexto));

                // Calcular la diferencia de ángulo entre el ángulo actual y el nuevo ángulo para el servo2 (arm)
                const diferenciaAnguloArm = nuevoAngulo - arm.rotation.z;

                // Rotar el brazo del servo2 (arm) alrededor del codo (elbow)
                arm.rotateOnWorldAxis(new THREE.Vector3(0, 0, -1), diferenciaAnguloArm);

                // Calcular la nueva posición del punto de conexión entre el lowerArm y el arm (punto de pivote)
                const pivotPoint = new THREE.Vector3(0, a1 / 2, 0); // Suponiendo que el punto de pivote está en la parte superior del lowerArm

                // Aplicar la rotación al punto de pivote del lowerArm
                pivotPoint.applyQuaternion(shoulder.quaternion);

                // Calcular la nueva posición del arm para que el punto de pivote del lowerArm y el arm permanezcan conectados
                arm.position.sub(pivotPoint);
                arm.position.applyAxisAngle(new THREE.Vector3(0, 0, -1), diferenciaAnguloArm);
                arm.position.add(pivotPoint);

                // Renderizar la escena para actualizar los cambios
                renderer.render(scene, camera);
            }
            
                function mover_servo22(nuevoAngulo) {

                // Calcular la diferencia de ángulo entre el ángulo actual y el nuevo ángulo para el servo2 (arm)
                const diferenciaAnguloArm = nuevoAngulo - arm.rotation.z;

                // Rotar el brazo del servo2 (arm) alrededor del codo (elbow)
                arm.rotateOnWorldAxis(new THREE.Vector3(0, 0, -1), diferenciaAnguloArm);

                // Calcular la nueva posición del punto de conexión entre el lowerArm y el arm (punto de pivote)
                const pivotPoint = new THREE.Vector3(0, a1 / 2, 0); // Suponiendo que el punto de pivote está en la parte superior del lowerArm

                // Aplicar la rotación al punto de pivote del lowerArm
                pivotPoint.applyQuaternion(shoulder.quaternion);

                // Calcular la nueva posición del arm para que el punto de pivote del lowerArm y el arm permanezcan conectados
                arm.position.sub(pivotPoint);
                arm.position.applyAxisAngle(new THREE.Vector3(0, 0, -1), diferenciaAnguloArm);
                arm.position.add(pivotPoint);

                // Renderizar la escena para actualizar los cambios
                renderer.render(scene, camera);
            }


           function mover_motores() {
               const num = parseInt(document.getElementById("MiCampoDeTexto2").value);
               const num1 = parseInt(document.getElementById("MiCampoDeTexto3").value);
               
               if (isNaN(num) || isNaN(num1) || (num !== 0 && num !== 1) || (num1 !== 0 && num1 !== 1)) {
              document.getElementById("error").innerHTML = "Error: Los valores ingresados para los motores no son válidos. Ingrese 1 o 0";
              } else {
                   
                    document.getElementById("error").innerHTML = "";
 
                   if (num == 0  && num1 === 1 ) {
                            // Cambiar color de la llanta 1
                            wheel1.material.color.setHex(0x00ff00);
                            wheel2.material.color.setHex(0xFF0000);
                            renderer.render(scene, camera);
                        } else if (num == 1  && num1 === 0) {
                            // Cambiar color de la llanta 2
                            wheel2.material.color.setHex(0x00ff00);
                            wheel1.material.color.setHex(0x0000FF);
                            renderer.render(scene, camera);
                        } else if (num === 1 && num1 === 1) {
                            wheel1.material.color.setHex(0x00ff00);
                            renderer.render(scene, camera);
                            wheel2.material.color.setHex(0x00ff00);
                            renderer.render(scene, camera);
                        } else if (num === 0 && num1 === 0) {
                            // Restaurar color de la llanta 1 y 2 
                            wheel1.material.color.setHex(0x555555);
                            wheel2.material.color.setHex(0x555555);
                            renderer.render(scene, camera);
                        } 
                    }
               }
               
               function mover_motoresB( num , num1) {
               
               if (isNaN(num) || isNaN(num1) || (num !== 0 && num !== 1) || (num1 !== 0 && num1 !== 1)) {
              document.getElementById("error").innerHTML = "Error: Los valores ingresados para los motores no son válidos. Ingrese 1 o 0";
              } else {
                   
                    document.getElementById("error").innerHTML = "";
 
                   if (num == 0  && num1 === 1 ) {
                            // Cambiar color de la llanta 1
                            wheel1.material.color.setHex(0x00ff00);
                            wheel2.material.color.setHex(0xFF0000);
                            renderer.render(scene, camera);
                        } else if (num == 1  && num1 === 0) {
                            // Cambiar color de la llanta 2
                            wheel2.material.color.setHex(0x00ff00);
                            wheel1.material.color.setHex(0x0000FF);
                            renderer.render(scene, camera);
                        } else if (num === 1 && num1 === 1) {
                            wheel1.material.color.setHex(0x00ff00);
                            renderer.render(scene, camera);
                            wheel2.material.color.setHex(0x00ff00);
                            renderer.render(scene, camera);
                        } else if (num === 0 && num1 === 0) {
                            // Restaurar color de la llanta 1 y 2 
                            wheel1.material.color.setHex(0x555555);
                            wheel2.material.color.setHex(0x555555);
                            renderer.render(scene, camera);
                        } 
                    }
               }
               
function baile() {
    let cnte = 1;
    let cte = 0;

    // Función para ejecutar la secuencia de movimientos
    function ejecutarMovimientos() {
        // Llama a mover_motoresB con cnte y cte
        mover_motoresB(cnte, cte);

        setTimeout(function() {
            // Cambia los argumentos y llama a mover_motoresB con cte y cnte
            mover_motoresB(cte, cnte);

            setTimeout(function() {
                // Cambia los argumentos y llama a mover_motoresB con cnte y cnte
                mover_motoresB(cnte, cnte);

                setTimeout(function() {
                    // Cambia los argumentos y llama a mover_motoresB con cte y cte nuevamente
                    mover_motoresB(cte, cte);

                    setTimeout(function() {
                        // Después de los movimientos de motores, mover el servo a -90
                        mover_servo11(-110);

                        setTimeout(function() {
                            // Después de mover a -90, mover el servo a -10
                            mover_servo11(-10);
                        }, 2000); // Espera 2 segundos antes de mover a -10
                    }, 2000); // Espera 2 segundos antes de mover los servos
                }, 2000); // Espera 2 segundos antes de mover los motores por segunda vez
            }, 2000); // Espera 2 segundos antes de mover los motores por primera vez
        }, 2000); // Espera 2 segundos antes de mover los motores por primera vez
    }

    // Espera 3 segundos antes de comenzar el ciclo
    setTimeout(function() {
        // Repite la secuencia de movimientos tres veces usando un bucle for
        for (let i = 0; i < 3; i++) {
            setTimeout(ejecutarMovimientos, i * 8000); // Espera 16 segundos entre cada repetición
        }

        // Después de completar las tres repeticiones, mover el servo a 10 grados
        setTimeout(function() {
            mover_servo22(-30);
        }, 3 * 16000); // Espera 3 ciclos completos antes de mover a 10 grados
    }, 1000); // Espera 1 segundos antes de iniciar los movimientos
}


		// Function to calculate inverse kinematics
		function inv_kin(P) {
			const x03 = -P.x;
			const z03 = P.y;
			const y03 = P.z;
			const th1 = Math.atan2(y03, x03);
			const r1 = Math.sqrt(x03 ** 2 + y03 ** 2);
			const r2 = -(z03 - a1);
			const phi2 = Math.atan2(r2, r1);
			const r3 = Math.sqrt(r1 ** 2 + r2 ** 2);
            const phi1 = Math.acos((a3 ** 2 - a2 ** 2 - r3 ** 2) / (-2 * a2 * r3));
			const th2 = phi2 - phi1;
			const phi3 = Math.acos((r3 ** 2 - a2 ** 2 - a3 ** 2) / (-2 * a2 * a3));
			const th3 = Math.PI - phi3;
			return [th1, th2, th3];
		}

		// Function for Bezier interpolation between two points
            function bezier2(P0, P1, t) {
			const R = P0.clone().multiplyScalar(1 - t).add(P1.clone().multiplyScalar(t));
			return R;
		}
		
		</script>

	</body>
</html>