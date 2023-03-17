from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from web3 import Web3
from .models import Investment

@login_required
@user_passes_test(lambda u: u.is_investor)
def inversiones(request):
    inversiones = Investment.objects.all()
    return render(request, 'inversiones.html', {'inversiones': inversiones})

""" def invertir(request):
    if request.method == 'POST':
        form = InversionForm(request.POST)
        if form.is_valid():
            cantidad_invertida = form.cleaned_data['cantidad_invertida']
            direccion_billetera = form.cleaned_data['direccion_billetera']
            # Realiza la inversión en el smart contract
            try:
                my_contract.functions.invertir().transact({'from': direccion_billetera, 'value': cantidad_invertida})
                # Redirige a una página de éxito
                return render(request, 'inversion_exitosa.html')
            except Web3.exceptions.ContractLogicError as e:
                # Si la transacción falla, renderiza la página de error correspondiente
                return render(request, 'inversion_fallida.html', {'error': str(e)})
    else:
        form = InversionForm()
    return render(request, 'formulario_inversion.html', {'form': form}) """