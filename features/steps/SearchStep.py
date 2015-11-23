from pages.GooglePage import GooglePage

@given(u'I am on Google Site')
def step_impl(context):
    context.page_object = GooglePage(context.driver)
    context.page_object.open_url()

@when(u'I search for {query}')
def step_impl(context, query):
    context.page_object.enter_search_term(query)

@then(u'I must see {name} on results')
def step_impl(context, name):
    context.page_object.check_result(name)
