from django.db import models

class BurnoutSurvey(models.Model):
    # Pontuação padrão (para perguntas com ordem direta)
    NEVER = 1
    RARELY = 2
    SOMETIMES = 3
    OFTEN = 4
    ALWAYS = 5

    # Pontuação alternativa (para perguntas com ordem inversa)
    NEVER_ALT = 5
    RARELY_ALT = 4
    SOMETIMES_ALT = 3
    OFTEN_ALT = 2
    ALWAYS_ALT = 1

    STATEMENT_CHOICES_INVERSE = [
        (NEVER_ALT, "Nunca"),
        (RARELY_ALT, "Raramente"),
        (SOMETIMES_ALT, "Às Vezes"),
        (OFTEN_ALT, "Frequentemente"),
        (ALWAYS_ALT, "Sempre"),
    ]

    STATEMENT_CHOICES_DIRECT = [
        (NEVER, "Nunca"),
        (RARELY, "Raramente"),
        (SOMETIMES, "Às Vezes"),
        (OFTEN, "Frequentemente"),
        (ALWAYS, "Sempre"),
    ]

    statement_1 = models.IntegerField(
        choices=STATEMENT_CHOICES_DIRECT,  # Ordem direta (1-5)
        verbose_name="1. Costumo me sentir esgotado(a) emocionalmente em relação ao meu trabalho."
    )
    statement_2 = models.IntegerField(
        choices=STATEMENT_CHOICES_INVERSE,  # Ordem inversa (5-1)
        verbose_name="2. Sinto que consigo lidar emocionalmente com as demandas do trabalho."
    )
    statement_3 = models.IntegerField(
        choices=STATEMENT_CHOICES_DIRECT,  # Ordem direta (1-5)
        verbose_name="3. Sinto que a carga de trabalho está impactando minha saúde física, como dores, cansaço excessivo ou outros sintomas."
    )
    statement_4 = models.IntegerField(
        choices=STATEMENT_CHOICES_INVERSE,  # Ordem inversa (5-1)
        verbose_name="4. Consigo me desconectar emocionalmente do trabalho quando estou fora do expediente."
    )
    statement_5 = models.IntegerField(
        choices=STATEMENT_CHOICES_INVERSE,  # Ordem inversa (5-1)
        verbose_name="5. Mantenho distância emocional dos problemas dos outros com facilidade."
    )
    statement_6 = models.IntegerField(
        choices=STATEMENT_CHOICES_INVERSE,  # Ordem inversa (5-1)
        verbose_name="6. Sinto-me tranquilo(a) ao lidar com as pessoas no meu ambiente de trabalho."
    )
    statement_7 = models.IntegerField(
        choices=STATEMENT_CHOICES_INVERSE,  # Ordem inversa (5-1)
        verbose_name="7. Me preocupo genuinamente com o bem-estar dos colegas de trabalho."
    )
    statement_8 = models.IntegerField(
        choices=STATEMENT_CHOICES_INVERSE,  # Ordem inversa (5-1)
        verbose_name="8. Sinto-me emocionalmente equilibrado(a) ao lidar com colegas, gestores ou clientes no ambiente de trabalho."
    )
    statement_9 = models.IntegerField(
        choices=STATEMENT_CHOICES_DIRECT,  # Ordem direta (1-5)
        verbose_name="9. Não sinto mais tanto amor pelo meu trabalho como antes."
    )
    statement_10 = models.IntegerField(
        choices=STATEMENT_CHOICES_DIRECT,  # Ordem direta (1-5)
        verbose_name="10. Não acredito mais naquilo que realizo profissionalmente."
    )
    statement_11 = models.IntegerField(
        choices=STATEMENT_CHOICES_INVERSE,  # Ordem inversa (5-1)
        verbose_name="11. Sinto que continuo entusiasmado(a) e motivado(a) em relação ao meu trabalho."
    )
    statement_12 = models.IntegerField(
        choices=STATEMENT_CHOICES_INVERSE,  # Ordem inversa (5-1)
        verbose_name="12. Sinto que meu trabalho atual proporciona um senso de propósito ou realização pessoal."
    )

    def total_score(self):
        score = (
            self.statement_1 + self.statement_2 + self.statement_3 + 
            self.statement_4 + self.statement_5 + 
            self.statement_6 + self.statement_7 + 
            self.statement_8 + self.statement_9 + 
            self.statement_10 + self.statement_11 + 
            self.statement_12 
        )
        return score
