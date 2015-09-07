from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

import braintree
import requests
import json

@login_required
def clienttoken(request):
    import ipdb; ipdb.set_trace()
    result = braintree.Customer.create({
        "first_name": "Jen",
        "last_name": "Smith",
        "company": "Braintree",
        "email": "jen@example.com",
        "phone": "312.555.1234",
        "fax": "614.555.5678",
        "website": "www.example.com",
        "credit_card": {
            "cardholder_name": "Jeen",
            "number": "4000111111111115",
            "expiration_date": "05/2019",
            "options": {
                "verify_card": True,
            },
        },
    })
    client_token = braintree.ClientToken.generate({"customer_id": result.customer.id})
    request.session['customer_id'] = result.customer.id
    return render(request, "braintreeapp/checkout.html", {"client_token": client_token})


@csrf_exempt
def checkout(request):
    import ipdb; ipdb.set_trace()
    customer_id = request.session['customer_id']
    nonce = request.POST['payment_method_nonce']
    # result = braintree.Customer.create({
    #     "first_name": "Fred",
    #     "last_name": "Jones",
    #     "credit_card": {
    #         "payment_method_nonce": nonce,
    #         "options": {
    #             "verify_card": True
    #         }
    #     }
    # })
    result = braintree.PaymentMethod.create({
        "customer_id": customer_id,
        "payment_method_nonce": nonce,
        "options": {
            "verify_card": True,
            "verification_merchant_account_id": "abc1we",
        }
    })
    result = braintree.Transaction.sale({
        "credit_card": {
            "number": "4000111111111115",
            "expiration_date": "05/2019",
            "cvv": "201"
        },
        "amount": "4001.00",
        "options": {
            # "verify_card": "true",
            "submit_for_settlement": "true"
        }
    })
    return HttpResponse(result.is_sucess)
