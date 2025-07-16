# from transformers import AutoTokenizer, AutoModelForCausalLM
# import torch
import pyautogui
import pyperclip
import time
import random

# def ask_for_ia(prompt):
#     model_id = 'Llama-3.2-3B-Instruct'
#     model_path = f'./models/{model_id}'

#     tokenizer = AutoTokenizer.from_pretrained(model_path)

#     messages = [
#         {"role": "user", "content": prompt},
#     ]
#     inputs = tokenizer.apply_chat_template(
#         messages, add_generation_prompt=True, return_tensors="pt", return_dict=True
#     )

#     model = AutoModelForCausalLM.from_pretrained(
#         model_path, device_map="auto", torch_dtype=torch.bfloat16
#     )

#     outputs = model.generate(**inputs.to(model.device), max_new_tokens=100)
#     outputs = tokenizer.batch_decode(outputs[:, inputs["input_ids"].shape[-1] :], skip_special_tokens=True)
    
#     return outputs[0]


def digitar(texto, intervalo_medio=0.03, variacao=0.015):
    for caractere in texto:
        pyautogui.write(caractere)
        time.sleep(random.uniform(intervalo_medio - variacao, intervalo_medio + variacao))


def main():
    texto_copiado = pyperclip.paste()
    pyautogui.sleep(5)  # Espera meio segundo para garantir que o texto foi copiado corretamente
    # if texto_copiado is None:
    #     print('Nenhum texto copiado encontrado.')
    #     return

    # pergunta = f'Responda a seguinte pergunta: {texto_copiado}, por favor, de forma clara e objetiva. Seu texto deve ser curto, direto e sem rodeios. Não use emojis ou caracteres especiais. Responda apenas com o texto necessário para responder a pergunta.'
    # resposta = ask_for_ia(pergunta)

    digitar(texto_copiado)


if __name__ == '__main__':
    main()
