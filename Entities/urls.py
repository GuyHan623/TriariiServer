from django.urls import path
from .views import DivisionViews, MessageViews, AgentViews, DispatchViews

urlpatterns = [
    path('divisions/', DivisionViews.as_view(), name='divisions'),
    path('divisions/create/', DivisionViews.as_view(), name='division-create'),
    path('messages/', MessageViews.as_view(), name='messages'),
    path('messages/create/', MessageViews.as_view(), name='message-create'),
    path('agents/', AgentViews.as_view(), name='agents'),
    path('agents/create/', AgentViews.as_view(), name='agent-create'),
    path('dispatches/', DispatchViews.as_view(), name='dispatches'),
]