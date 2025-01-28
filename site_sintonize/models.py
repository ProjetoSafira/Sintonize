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

    statement_1 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="1. Com que frequência você sente que não consegue lidar emocionalmente com as demandas do trabalho?.")
    statement_2 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="2. Você sente que perdeu o entusiasmo ou a motivação que tinha em relação ao seu trabalho?.")
    statement_3 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="3. Sente-se frequentemente ansioso(a) ou frustrado(a) em relação ao trabalho?.")
    statement_4 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="4. Com que frequência você se sente irritado(a) ou impaciente com colegas, gestores ou clientes?.")
    statement_5 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="5. Você sente dificuldade em se desconectar emocionalmente do trabalho, mesmo fora do expediente?.")
    statement_6 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="6. Após o expediente, com que frequência você se sente fisicamente exausto(a)?.")
    statement_7 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="7. Ao acordar, você sente que não recuperou a necessidade de energia, mesmo após uma noite de descanso?.")
    statement_8 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="8.Você sente que a carga de trabalho está impactando sua saúde física, como dores, cansaço excessivo ou outros sintomas?.")
    statement_9 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="9. Você percebe alterações no seu apetite ou padrão de sono devido ao trabalho?.")
    statement_10 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="10. Você sente que seu esforço ou desempenho no trabalho não é devidamente reconhecido ou valorizado?.")
    statement_11 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="11. Você acredita que seu trabalho atual proporciona um senso de propósito ou realização pessoal?.")
    statement_12 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="12. Você considera que os pagamentos ou benefícios recebidos são proporcionais ao critério do trabalho?.")
    statement_13 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="13. Você acredita que o ambiente de trabalho contribui positivamente para seu bem-estar mental e físico?.")
    statement_14 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="14. Você sente que pode contar com o apoio de seus colegas ou superiores em momentos de dificuldade?.")
    statement_15 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="15. Você sente que consegue equilibrar suas responsabilidades profissionais com sua vida pessoal?.")
    statement_16 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="16. Com que frequência você sente que o tempo disponível para realizar suas tarefas no trabalho é insuficiente?.")
    statement_17 = models.IntegerField(choices=STATEMENT_CHOICES, verbose_name="17. Você percebe que o trabalho interfere na sua capacidade de cuidar de si mesmo(a) ou de outras áreas importantes da sua vida?.")


    def total_score(self):
        score = (
            self.statement_1 + self.statement_2 + self.statement_3 + 
            self.statement_4 + self.statement_5 + 
            self.statement_6 + self.statement_7 + 
            self.statement_8 + self.statement_9 + 
            self.statement_10 + self.statement_11 + 
            self.statement_12 + self.statement_13 + 
            self.statement_14 + self.statement_15 + 
            self.statement_16 + self.statement_17 
        )
        return score
