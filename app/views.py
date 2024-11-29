from rest_framework import generics

from .models import Candidates
from .serializers import SerializedCandidate


class CandidatesView(generics.ListCreateAPIView):
    """
    Candidat chez AriMayi\n...
    """
    queryset = Candidates.objects.all()
    serializer_class = SerializedCandidate