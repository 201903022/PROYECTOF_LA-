// Gramatica a trabajar 
/**
 * S -> zMNz
 * M -> aMa
 * M -> z
 * N -> bNb
 * N -> z
 * [ [ M,[ [a,M,a],[z] ] ] { M:[[a,M,a],[z]],N:[[b,N,b],[z]] }
 * a, if a in Terminales: 
 * S, if S in noTerminales
 */

const noTerminales = [ 'a', 'z', 'b' ]
const terminales = [ 'S', 'M', 'N']
const inicial = {
    tipo: "no terminal",
    valor: "S"
}

const producciones = [
    { 
        name: "S",
        rules : [
            [
                {
                    tipo: "no terminal",
                    valor: "z"
                },
                {
                    tipo: "terminal",
                    valor: "M"
                },
                {
                    tipo: "terminal",
                    valor: "N"
                },
                {
                    tipo: "no terminal",
                    valor: "z"
                }
            ]
        ],
    },
    
    { 
        name : "M",
        rules : [
            [
                {
                    tipo: "no terminal",
                    valor: "a"
                },
                {
                    tipo: "terminal",
                    valor: "M"
                },
                {
                    tipo: "no terminal",
                    valor: "a"
                }
            ],
            [
                {
                    tipo: "no terminal",
                    valor: "z"
                }
            ]
        ],
    },
    {
        name: "N",
        rules : [
            [
                {
                    tipo: "no terminal",
                    valor: "b"
                },
                {
                    tipo: "terminal",
                    valor: "N"
                },
                {
                    tipo: "no terminal",
                    valor: "b"
                }
            ],
            [
                {
                    tipo: "no terminal",
                    valor: "z"
                }
            ]
        ]
    }
]

let input = "zazabzbz"

let i = 0;
let input_length = input.length;
let stack = [];
let state = 'i';

while (i < input_length) {
    
    switch (state) {
        case "i":
            // i no avanza, significa que no leemos nada de la cadena de entrada
            // no se saca nada de la pila, unicamente introducimos '#'
            let stack_element_i = {
                tipo: "no terminal",
                valor: "#"
            }
            stack.unshift(stack_element_i);
            state = "p";
            break;

        case "p":
            // i no avanza, no leemos nada de la cadena de entrada
            // no se saca nada de la pila, para este momento la pila se encuentra asi: [ # ]

            // Introducimos el simbolo no terminal inicial a la pila
            let stack_element_p = inicial;
            stack.unshift(stack_element_p);

            // la pila en este momento: [ S, # ]
            // transicion al estado especificado
            state = "q";
            break;

        case "q":
            for (let j = 0; j < producciones.length; j++) {
                let current_production = producciones[j];
                let stack_top = stack[0];
                if (stack_top.tipo === "no terminal" && stack_top.valor === current_production.name) {
                    if (current_production.rules.length === 1) {
                        stack.shift();
                        // pila en este momento (para el caso de S): [ # ] 
                        for (let k = current_production.rules.length; k >= 0; k--) {
                            let aux = current_production.rules[k];
                            stack.unshift(aux) 
                        }
                        // pila quedaria (para el caso de S): [ z M N z # ]
                    }
                    else {
                        let rule = null;
                        let currentChar = input.charAt(i);
                        for (let k = 0; k < current_production.rules.length; k++) {
                            let currentRule = current_production.rules[k];
                            if (currentRule[0].valor === currentChar) {
                                rule = currentRule;
                            }   
                        }

                        stack.shift();
                        for (let k = rule.length; k >= 0; k--) {
                            let aux = rules[k];
                            stack.unshift(aux) 
                        }
                        // ejemplo de como quedaria la pila en este momento: [ z N z # ]
                    }
                }
                else if (stack_top.tipo === "terminal" && stack_top.valor === input.charAt(i)) {
                    i++;
                    stack.shift();
                    // ejemplo de como quedaria la pila en este momento: [ N z # ]  q,a,a,q,
                }
                else if (stack_top.tipo === "terminal" && stack_top.valor != input.charAt(i)) {
                    // Error, la cadena de entrada no se adapta al automata con pila
                }
                else if (stack_top.tipo === "no terminal" && stack_top.valor === "#") {
                    stack.shift()
                    // pila nos queda: [ ]
                    state = "f";
                }
            }
            break;

        case "f":
            if (i === input_length) {
                // aceptamos
            }
            else {
                // error, no se adapta
            }
            break;        
    }

}
