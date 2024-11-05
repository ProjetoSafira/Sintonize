from django.db import models

class BurnoutSurvey(models.Model):
    NEVER = 1
    RARELY = 2
    SOMETIMES = 3
    OFTEN = 4
    ALWAYS = 5

    STATEMENT_CHOICES = [
        (NEVER, "Nunca"),
        (RARELY, "Raramente"),
        (SOMETIMES, "Às Vezes"),
        (OFTEN, "Frequentemente"),
        (ALWAYS, "Sempre"),
    ]

    statement_1 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="1. Eu me sinto emocionalmente esgotado.")
    statement_2 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="2. Eu me sinto sobrecarregado de trabalho.")
    statement_3 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="3. Eu me sinto menos competente no meu trabalho.")
    statement_4 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="4. Eu me sinto isolado no meu ambiente de trabalho.")
    statement_5 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="5. Eu tenho dificuldade em relaxar após o trabalho.")
    statement_6 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="6. Eu me sinto apático em relação a atividades que costumava gostar.")
    statement_7 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="7. Eu sinto que as minhas emoções estão fora de controle.")
    statement_8 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="8. Eu me sinto menos produtivo do que antes.")
    statement_9 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="9. Eu fico facilmente irritado ou frustrado.")
    statement_10 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="10. Eu tenho dificuldade em me concentrar em tarefas simples.")
    statement_11 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="11. Não sinto mais tanto amor pelo meu trabalho como antes.")
    statement_12 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="12. Não acredito mais naquilo que realizo profissionalmente.")
    statement_13 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="13. Penso que não importa o que eu faça, nada vai mudar no meu trabalho.")
    statement_14 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="14. As pessoas me culpam pelos seus problemas.")
    statement_15 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="15. Sinto-me responsável pelos problemas das pessoas que atendo.")
    statement_16 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="16. Tenho me sentido mais estressado(a) com as pessoas que atendo.")
    statement_17 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="17. Estou no emprego apenas por causa do salário.")
    statement_18 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="18. Sinto-me sem forças para conseguir algum resultado significante.")
    statement_19 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="19. Não acredito mais na profissão que exerço.")
    statement_20 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="20. Envolvo-me com facilidade nos problemas dos outros.")

    def total_score(self):
        score = (
            self.statement_1 + self.statement_2 + self.statement_3 + 
            self.statement_4 + self.statement_5 + 
            self.statement_6 + self.statement_7 + 
            self.statement_8 + self.statement_9 + 
            self.statement_10 + self.statement_11 + 
            self.statement_12 + self.statement_13 + 
            self.statement_14 + self.statement_15 + 
            self.statement_16 + self.statement_17 + 
            self.statement_18 + self.statement_19 + 
            self.statement_20
        )
        return score
